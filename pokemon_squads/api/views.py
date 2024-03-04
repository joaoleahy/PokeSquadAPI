from rest_framework import status, views
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from pokemon_squads.domain.use_cases import CreateTeamUseCase
from pokemon_squads.infrastructure.pokemon_api import PokeAPI
from pokemon_squads.infrastructure.repositories import DjangoORMTeamRepository
from pokemon_squads.models import Team
from .serializers import TeamSerializer

class TeamListView(views.APIView):
    @swagger_auto_schema(
        operation_summary="List all Teams",
        operation_description="Retrieve a list of all Pokemon teams available in the database.",
        responses={200: openapi.Response('A list of Pokemon Teams', TeamSerializer(many=True))},
        tags=['Teams'],
    )
    def get(self, request):
        teams = Team.objects.all()
        formatted_teams = {}
        for team in teams:
            serializer = TeamSerializer(team)
            serialized_data = serializer.data
            formatted_data = {
                'owner': serialized_data['owner'],
                'pokemons': serialized_data['pokemons']
            }
            formatted_teams[str(team.id)] = formatted_data
        return Response(formatted_teams)



class TeamRetrieveView(views.APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve Team by User",
        operation_description="Retrieve a specific team by the team's owner username.",
        responses={
            200: openapi.Response('Team details', TeamSerializer()),
            404: 'Team not found'
        },
        tags=['Teams'],
    )

    def get(self, request, user):
        try:
            team = Team.objects.get(user=user)
            serializer = TeamSerializer(team)
            serialized_data = serializer.data
            
            formatted_data = {
                'owner': serialized_data.get('owner'),
                'pokemons': serialized_data.get('pokemons', [])
            }

            return Response(formatted_data)
        except Team.DoesNotExist:
            return Response({'message': 'Team not found.'}, status=status.HTTP_404_NOT_FOUND)


class TeamCreateView(views.APIView):
    @swagger_auto_schema(
        operation_summary="Create a New Team",
        operation_description="Create a new Pokemon team with the provided username and list of Pokemons.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['user', 'team'],
            properties={
                'user': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'team': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING), description='List of Pokemon names')
            },
        ),
        responses={201: openapi.Response('Team created successfully', TeamSerializer())},
        tags=['Teams'],
    )

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            pokemon_names = serializer.validated_data.get('team', [])
            
            pokemon_api = PokeAPI()
            repository = DjangoORMTeamRepository()
            use_case = CreateTeamUseCase(repository, pokemon_api)
            
            try:
                team = use_case.execute(user, pokemon_names)
                return Response({'message': f'Team created successfully for user {user}', 'team_id': team.id}, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

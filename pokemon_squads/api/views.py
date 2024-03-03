from rest_framework import status, views
from rest_framework.response import Response
from pokemon_squads.domain.use_cases import CreateTeamUseCase
from pokemon_squads.infrastructure.pokemon_api import PokeAPI
from pokemon_squads.infrastructure.repositories import DjangoORMTeamRepository
from pokemon_squads.models import Team
from .serializers import TeamSerializer

class TeamListView(views.APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

class TeamRetrieveView(views.APIView):
    def get(self, request, user):
        try:
            team = Team.objects.get(user=user)
            serializer = TeamSerializer(team)
            return Response(serializer.data)
        except Team.DoesNotExist:
            return Response({'message': 'Time não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

class TeamCreateView(views.APIView):
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
                return Response(TeamSerializer(team).data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

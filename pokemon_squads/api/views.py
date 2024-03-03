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

class TeamCreateView(views.APIView):
    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            pokemons = serializer.validated_data.get('pokemons', [])
            
            pokemon_api = PokeAPI()
            repository = DjangoORMTeamRepository()
            use_case = CreateTeamUseCase(repository, pokemon_api)
            
            try:
                team = use_case.execute(user, [pokemon['name'] for pokemon in pokemons])
                return Response(TeamSerializer(team).data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

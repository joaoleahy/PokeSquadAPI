from typing import List, Dict

from pokemon_squads.domain.repositories import TeamRepository
from pokemon_squads.models import Team, Pokemon

class DjangoORMTeamRepository(TeamRepository):
    def add_team(self, user: str, pokemons_data: List[Dict]) -> Team:
        team = Team.objects.create(user=user)
        for pokemon_data in pokemons_data:
            Pokemon.objects.create(team=team, **pokemon_data)
        return team

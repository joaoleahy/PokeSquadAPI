from typing import List, Dict

from pokemon_squads.domain.repositories import TeamRepository
from pokemon_squads.models import Team, Pokemon

class DjangoORMTeamRepository(TeamRepository):
    def add_team(self, user: str, pokemon_data_list: List[Dict]) -> Team:
        team = Team.objects.create(user=user)

        for pokemon_data in pokemon_data_list:
            Pokemon.objects.create(team=team, **pokemon_data)

        return team
    
    def exists(self, user):
        return Team.objects.filter(user=user).exists()
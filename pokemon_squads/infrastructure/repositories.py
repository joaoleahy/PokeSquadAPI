from typing import List, Dict

from pokemon_squads.domain.repositories import TeamRepository
from pokemon_squads.models import Team, Pokemon
from pokemon_squads.infrastructure.pokemon_api import PokeAPI

class DjangoORMTeamRepository(TeamRepository):
    def add_team(self, user: str, pokemon_names: List[str]) -> Team:
        team = Team.objects.create(user=user)
        poke_api = PokeAPI()

        for name in pokemon_names:
            pokemon_data = poke_api.get_pokemon_data(name)
            if pokemon_data:
                Pokemon.objects.create(team=team, **pokemon_data)
            else:
                print(f"Pokemon {name} not found in PokeAPI.")
        return team
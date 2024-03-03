from .repositories import TeamRepository
from pokemon_squads.infrastructure.pokemon_api import PokeAPI

class CreateTeamUseCase:
    def __init__(self, team_repository: TeamRepository, pokemon_api: PokeAPI):
        self.team_repository = team_repository
        self.pokemon_api = pokemon_api

    def execute(self, user, pokemon_names):
        pokemons_data = []
        for name in pokemon_names:
            data = self.pokemon_api.get_pokemon_data(name)
            if data:
                pokemons_data.append(data)
            else:
                raise ValueError(f"Pokemon with name '{name}' not found.")
        team = self.team_repository.add_team(user, pokemons_data)
        return team

from rest_framework.exceptions import ValidationError
from .repositories import TeamRepository
from ..infrastructure.pokemon_api import PokeAPI

class CreateTeamUseCase:
    MAX_POKEMONS_PER_TEAM = 6

    def __init__(self, team_repository: TeamRepository, pokemon_api: PokeAPI):
        self.team_repository = team_repository
        self.pokemon_api = pokemon_api

    def execute(self, user, pokemon_names):
        self._validate_user_does_not_have_team(user)
        self._validate_pokemon_names(pokemon_names)
        self._validate_team_size(pokemon_names)
        self._validate_no_duplicate_pokemons(pokemon_names)
        
        pokemons_data = self._get_pokemons_data(pokemon_names)
        team = self.team_repository.add_team(user, pokemons_data)
        return team

    def _validate_user_does_not_have_team(self, user):
        if self.team_repository.exists(user):
            raise ValidationError({'user': [f"User '{user}' already has a team."]})

    def _validate_pokemon_names(self, pokemon_names):
        if not pokemon_names:
            raise ValidationError({'team': ["Pokémon names must be provided."]})

    def _validate_team_size(self, pokemon_names):
        if len(pokemon_names) > self.MAX_POKEMONS_PER_TEAM:
            raise ValidationError({'team': [f"A team cannot have more than {self.MAX_POKEMONS_PER_TEAM} pokémons."]})

    def _validate_no_duplicate_pokemons(self, pokemon_names):
        if len(pokemon_names) != len(set(pokemon_names)):
            raise ValidationError({'team': ["Duplicate pokémons are not allowed in a team."]})

    def _get_pokemons_data(self, pokemon_names):
        pokemons_data = []
        for name in pokemon_names:
            data = self.pokemon_api.get_pokemon_data(name)
            if not data:
                raise ValidationError({'team': [f"Pokémon '{name}' not found."]})
            pokemons_data.append(data)
        return pokemons_data

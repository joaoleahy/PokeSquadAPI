from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from pokemon_squads.models import Team, Pokemon
from pokemon_squads.infrastructure.pokemon_api import PokeAPI

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['poke_id', 'name', 'height', 'weight']

class TeamSerializer(serializers.ModelSerializer):
    team = serializers.ListField(child=serializers.CharField(), write_only=True, required=False)
    pokemons = PokemonSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'user', 'team', 'pokemons']

    def create(self, validated_data):
        pokemon_names = validated_data.pop('team')
        user = validated_data.get('user')
        team = Team.objects.create(user=user)
        poke_api = PokeAPI()

        for name in pokemon_names:
            pokemon_data = poke_api.get_pokemon_data(name)
            if pokemon_data:
                Pokemon.objects.create(team=team, **pokemon_data)
            else:
                raise ValidationError({'team': [f"Pokémon '{name}' not found."]})

        return team

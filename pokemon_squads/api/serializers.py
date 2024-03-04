from rest_framework import serializers
from pokemon_squads.models import Team, Pokemon
from pokemon_squads.infrastructure.pokemon_api import PokeAPI
from rest_framework.exceptions import ValidationError

class PokemonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='poke_id', read_only=True)

    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'weight', 'height']

class TeamSerializer(serializers.ModelSerializer):
    user = serializers.CharField(write_only=True)
    team = serializers.ListField(child=serializers.CharField(), write_only=True, required=False)
    pokemons = PokemonSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['user', 'team', 'pokemons']

    def create(self, validated_data):
        user = validated_data.pop('user')
        pokemon_names = validated_data.pop('team', [])
    
        team = Team(user=user)
    
        poke_api = PokeAPI()
        pokemons_to_create = []
        for name in pokemon_names:
            pokemon_data = poke_api.get_pokemon_data(name)
            if pokemon_data:
                pokemons_to_create.append(Pokemon(
                    team=team,
                    poke_id=pokemon_data['id'],
                    name=pokemon_data['name'],
                    weight=pokemon_data['weight'],
                    height=pokemon_data['height']
                ))
            else:
                raise ValidationError({'team': [f"Pokémon '{name}' not found."]})
    
        team.save()
        Pokemon.objects.bulk_create(pokemons_to_create) 

        return team

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['owner'] = instance.user
        return representation


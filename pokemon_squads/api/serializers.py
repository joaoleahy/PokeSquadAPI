from rest_framework import serializers
from pokemon_squads.models import Team, Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='poke_id', read_only=True)

    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'weight', 'height']

class TeamSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='user', read_only=True)
    pokemons = PokemonSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['owner', 'pokemons']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get('use_custom_format', False):
            return {
                str(instance.id): {
                    'owner': representation['owner'],
                    'pokemons': representation['pokemons']
                }
            }
        else:
            return representation


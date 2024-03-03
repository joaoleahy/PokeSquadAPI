from django.db import models

class Team(models.Model):
    user = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Pokemon(models.Model):
    team = models.ForeignKey(Team, related_name='pokemons', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    poke_id = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()

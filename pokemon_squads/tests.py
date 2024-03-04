from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Team, Pokemon

class PokemonModelTest(TestCase):

    def test_create_pokemon(self):
        team = Team.objects.create(user='Ash Ketchum')
        pokemon = Pokemon.objects.create(
            team=team,
            name='Pikachu',
            poke_id=25,
            height=4,
            weight=60
        )
        self.assertEqual(pokemon.name, 'Pikachu')

class TeamModelTest(TestCase):

    def test_create_team_with_pokemon(self):
        team = Team.objects.create(user='Ash Ketchum')
        Pokemon.objects.create(
            team=team,
            name='Pikachu',
            poke_id=25,
            height=4,
            weight=60
        )
        self.assertEqual(team.pokemons.count(), 1)

class TeamViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.team_list_url = reverse('team-list')
        self.team_create_url = reverse('team-create')

        self.team = Team.objects.create(user='Ash Ketchum')
        self.pokemon = Pokemon.objects.create(
            team=self.team,
            name='Pikachu',
            poke_id=25,
            height=4,
            weight=60
        )

    def test_get_team_list(self):
        response = self.client.get(self.team_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Team.objects.count())

    def test_create_team(self):
        data = {
            'user': 'Misty',
            'team': ['starmie', 'psyduck']
        }
        response = self.client.post(self.team_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 2)

    def test_team_creation_without_pokemon(self):
        data = {
            'user': 'Brock',
            'team': []
        }
        response = self.client.post(self.team_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_team_detail(self):
        team_detail_url = reverse('retrieve-team', kwargs={'user': self.team.user})
        response = self.client.get(team_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['owner'], self.team.user)
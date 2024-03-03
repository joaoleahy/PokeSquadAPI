import requests

class PokeAPI:
    BASE_URL = 'https://pokeapi.co/api/v2/pokemon/'

    def get_pokemon_data(self, name):
        response = requests.get(f"{self.BASE_URL}{name}")
        if response.status_code == 200:
            data = response.json()
            return {
                'poke_id': data['id'],
                'name': data['name'],
                'height': data['height'],
                'weight': data['weight']
            }
        else:
            return None
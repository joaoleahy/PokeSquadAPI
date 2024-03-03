import requests

def get_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url)
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

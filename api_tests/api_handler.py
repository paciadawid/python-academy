import requests


class APIHandler:
    url = "https://pokeapi.co/api/v2"
    pokemon_endpoint = "/pokemon"
    shape_endpoint = "/pokemon-shape"

    def get_pokemons(self, name_or_id="", params=None):
        response_body = requests.get(f"{self.url}{self.pokemon_endpoint}/{name_or_id}", params=params).json()
        return response_body

    def get_shapes(self, name_or_id="", params=None):
        response_body = requests.get(f"{self.url}{self.shape_endpoint}/{name_or_id}", params=params).json()
        return response_body

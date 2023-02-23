from locust import HttpUser, task, between
import random

class HelloWorldUser(HttpUser):

    wait_time = between(0.5, 2)

    @task
    def get_pokemons(self):
        self.client.get("/pokemon")

    @task
    def get_pokemon_by_id(self):
        poke_id = random.randint(1, 10)
        self.client.get(f"/pokemon/{poke_id}")

    @task
    def get_shapes(self):
        self.client.get("/pokemon-shape")

import requests
from django.core.management.base import BaseCommand, CommandError
#from pokemon.models import 

class Command(BaseCommand):
    help = 'Fetch and store all pokemons on a evolution chain'

    def add_arguments(self, parser):
        parser.add_argument('chain_id', type=int)

    def handle(self, *args, **options):
        url = "https://pokeapi.co/api/v2/evolution-chain/{id}".format(id=options["chain_id"])
        request = requests.get(url)
        if request.text == 'Not Found':
            raise ValueError("Chain not found")
        data = request.json()
        for p in self.chained_pokemons_gen(data["chain"]):
            print(p) 

    def fetch_pokemon(self, name):
        data = requests.get("https://pokeapi.co/api/v2/pokemon/{name}".format(name=name)).json()
        return  {"id": data["id"],
                "name": data["name"],
                "base_stats": data["stats"],
                "height": data["height"],
                "weight": data["weight"]}

    def chained_pokemons_gen(self, chain, preevolution = None):
        name = chain["species"]["name"]
        specie = {**self.fetch_pokemon(name),
                    "preevolution": preevolution}
        yield specie
        
        for c in chain["evolves_to"]:
            yield from self.chained_pokemons_gen(c, preevolution = name)
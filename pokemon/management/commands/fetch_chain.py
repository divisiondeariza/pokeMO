import requests
from django.core.management.base import BaseCommand, CommandError
from pokemon.models import Pokemon, StatSet, Stat

class PokemonHandler:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.stats = self.format_stats(data)
        self.height = data['height']
        self.weight = data['weight']
        self.preevolution = None
    
    def set_preevolution(self, preevolution):
        self.preevolution =  preevolution

    def store(self):
        stats = StatSet(**{ name:value for (name,value) in self.stats } )
        stats.save()
        pokemon = Pokemon(id = self.id,
                       name = self.name,
                       base_stats = stats,
                       height = self.height,
                       weight = self.weight)
        if self.preevolution and Pokemon.objects.filter(name=self.preevolution).exists():
            pokemon.preevolution = Pokemon.objects.get(name=self.preevolution)
        pokemon.save()
    

    def format_stats(self, data):
        return [(s['stat']['name'].replace('-', '_'), s['base_stat']) 
                for s in data['stats']]


class Command(BaseCommand):
    help = "Fetch and store all pokemons on a evolution chain"

    def add_arguments(self, parser):
        parser.add_argument('chain_id', type=int)

    def handle(self, *args, **options):
        url = "https://pokeapi.co/api/v2/evolution-chain/{id}".format(id=options["chain_id"])
        request = requests.get(url)
        if request.text == "Not Found":
            raise ValueError("Chain not found")
        data = request.json()
        for p in self.chained_pokemons_gen(data['chain']):
            p.store()

    def chained_pokemons_gen(self, chain, preevolution = None):
        name = chain['species']['name']
        data = requests.get("https://pokeapi.co/api/v2/pokemon/{name}".format(name=name)).json()
        pokemon_handler =  PokemonHandler(data)
        pokemon_handler.set_preevolution(preevolution)

        yield pokemon_handler
        
        for c in chain['evolves_to']:
            yield from self.chained_pokemons_gen(c, preevolution = name)


from pokemon.models import Pokemon
from rest_framework import viewsets
from pokemon.serializers import PokemonSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    lookup_field = 'name'

# Create your views here.

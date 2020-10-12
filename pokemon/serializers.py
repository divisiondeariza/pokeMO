from pokemon.models import Pokemon, StatSet
from rest_framework import serializers

class RelatedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'name']


class StatSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatSet
        exclude = ['id']

class PokemonSerializer(serializers.ModelSerializer):
    evolutions = RelatedPokemonSerializer(many=True)
    preevolution = RelatedPokemonSerializer()
    base_stats = StatSetSerializer()
    class Meta:
        model = Pokemon
        fields = '__all__'
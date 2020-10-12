from pokemon.models import Pokemon, StatSet, Stat
from rest_framework import serializers

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        exclude = ["id"]

class StatSetSerializer(serializers.ModelSerializer):
    hp = StatSerializer()
    attack = StatSerializer()
    defense = StatSerializer()
    special_attack = StatSerializer()
    special_defense = StatSerializer()
    speed = StatSerializer()
    class Meta:
        model = StatSet
        exclude = ["id"]

class PokemonSerializer(serializers.ModelSerializer):
    evolutions = serializers.StringRelatedField(many=True, read_only=True, required=False)
    stats = StatSetSerializer()
    class Meta:
        model = Pokemon
        fields = '__all__'
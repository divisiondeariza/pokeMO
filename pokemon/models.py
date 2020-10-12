from django.db import models

# Create your models here.
class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    base_stats =  models.OneToOneField('StatSet', on_delete=models.CASCADE)
    height = models.IntegerField()
    weight = models.IntegerField()
    preevolution = models.ForeignKey('self', on_delete=models.PROTECT, null=True, related_name="evolutions")

    def __str__(self):
            return self.name


class StatSet(models.Model):
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()



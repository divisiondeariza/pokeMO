from django.db import models

# Create your models here.
class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField("person's first name", max_length=255)
    stats =  models.OneToOneField('StatSet', on_delete=models.CASCADE)
    height = models.IntegerField()
    weight = models.IntegerField()
    preevolution = models.ForeignKey('self', on_delete=models.PROTECT, null=True, related_name="evolutions")


    def __str__(self):
            return self.name


class StatSet(models.Model):
    hp = models.ForeignKey('Stat', on_delete=models.CASCADE, related_name='hp')
    attack = models.ForeignKey('Stat', on_delete=models.CASCADE, related_name='attack')
    defense = models.ForeignKey('Stat', on_delete=models.CASCADE, related_name='defense')
    special_attack = models.ForeignKey('Stat', on_delete=models.CASCADE, related_name='special_attack')
    special_defense = models.ForeignKey('Stat', on_delete=models.CASCADE, related_name='special_defense')
    speed = models.ForeignKey('Stat', on_delete=models.CASCADE, related_name='speed')

class Stat(models.Model):
    base_stat =  models.IntegerField()
    effort = models.IntegerField()


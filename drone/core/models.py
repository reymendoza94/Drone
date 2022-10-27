from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator,RegexValidator

# Create your models here.

STATE = [
    ('idle', 'IDLE'),
    ('loading', 'LOADING'),
    ('loaded', 'LOADED'),
    ('delivering', 'DELIVERING'),
    ('delivered', 'DELIVERED'),
    ('returning', 'RETURNING')
]

MODEL = [
    ('lightweight', 'Lightweight'),
    ('middleweight', 'Middleweight'),
    ('cruiserweight', 'Cruiserweight'),
    ('heavyweight', 'Heavyweight'),
]

VALIDATOR_LIST = [RegexValidator('[A-Za-z0-9_-]', message="Only latters, number, underscore and dash")]
VALIDATOR_LIST2 = [RegexValidator('^[A-Z0-9_]+$', message="Only upper case latters , number and underscore")]


class Drone (models.Model):
    serial_number = models.CharField(max_length=100)
    model = models.CharField(max_length=15, choices=MODEL)
    weight_limit = models.FloatField(validators=[MaxValueValidator(500)]) #max limit 500
    battery_capacity = models.PositiveIntegerField()
    state = models.CharField(max_length=15, choices=STATE, default= 'idle')


class Medication (models.Model):
    name = models.CharField(max_length=100, validators=VALIDATOR_LIST)
    weight = models.FloatField(validators=[MaxValueValidator(500)])
    code = models.CharField(max_length=100, validators= VALIDATOR_LIST2) 
    image = models.ImageField()

class DispatchController (models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    medication = models.ManyToManyField(Medication)
from django.db import models
from django.core.validators import MaxValueValidator,RegexValidator

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

VALIDATOR_LIST = [RegexValidator('^[A-Za-z0-9_-]', message="Only latters, number, underscore and dash")]
VALIDATOR_LIST2 = [RegexValidator('^[A-Z0-9_]+$', message="Only upper case latters , number and underscore")]


class Drone (models.Model):
    serial_number = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=15, choices=MODEL)
    weight_limit = models.FloatField(verbose_name='weight in gr', validators=[MaxValueValidator(500)], default=500)
    battery_capacity = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    state = models.CharField(max_length=15, choices=STATE, default='idle')

    def __str__(self):
        return self.serial_number


class Medication (models.Model):
    name = models.CharField(max_length=100, validators=VALIDATOR_LIST)
    weight = models.FloatField(validators=[MaxValueValidator(500)])
    code = models.CharField(max_length=100, validators= VALIDATOR_LIST2, unique=True) 
    image = models.ImageField()

    def __str__(self):
        return self.code

class DispatchController (models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    medication = models.ManyToManyField(Medication)


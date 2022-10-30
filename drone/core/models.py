from importlib.metadata import requires
from re import I
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator,RegexValidator
from django.core.exceptions import ValidationError

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
    serial_number = models.CharField(max_length=100)
    model = models.CharField(max_length=15, choices=MODEL)
    weight_limit = models.FloatField(verbose_name='weight in gr', validators=[MaxValueValidator(500)], default = 0) #max limit 500
    battery_capacity = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    state = models.CharField(max_length=15, choices=STATE, default= 'idle')

    def __str__(self):
        return self.serial_number


class Medication (models.Model):
    name = models.CharField(max_length=100, validators=VALIDATOR_LIST)
    weight = models.FloatField(validators=[MaxValueValidator(500)])
    code = models.CharField(max_length=100, validators= VALIDATOR_LIST2) 
    image = models.ImageField()

    def __str__(self):
        return self.code

class DispatchController (models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    medication = models.ManyToManyField(Medication)

    def clean(self) -> None:
        if DispatchController.objects.filter(drone__id=self.drone.id):
            if self.drone.state != 'loading':
                raise ValidationError({"drone": "This drone are {}, cant not by used".format(self.drone.get_state_display())})

    def save(self, *args, **kwargs) -> None:
        self.drone.state = 'loading'
        self.drone.save()
        # total_w = 0
        # if self.medication:
        #     for v in self.medication.all():
        #         total_w += v.weight
        #     if total_w <= 500:
        #         self.drone.weight_limit = total_w
        #     else:
        #         raise ValidationError({"medication": "Limit weight"})
        super().save(self, *args, **kwargs)
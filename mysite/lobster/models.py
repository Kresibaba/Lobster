from django.db import models
from .choices import *

class Projects(models.Model):

    def __str__(self):
        return str(self.pk)

    name =  models.CharField(max_length = 200)                # Name of the project - defined by a user
    author = models.CharField(max_length = 200)               # Name of an author corresponds to an username
    create_date = models.DateTimeField(auto_now_add = True)   # Date and time when the project was created
    status = models.CharField(max_length = 100)               # Status of the project

    waste_type = models.IntegerField(choices = WASTE_TYPE_CHOICES, default = 1)
    weight_net = models.CharField(max_length = 200)           #Net weight of waste in kg
    volume_net = models.CharField(max_length = 200)           #Net volume is m3

class RNList(models.Model):

    # Coupling with Projects db
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE)

    # Radio spectrum of a waste - all values corresponds to specific activities in Becquerels per gram
    element_name = models.CharField(max_length=15)
    rn_name = models.CharField(max_length=15)
    rn_spec_activ = models.IntegerField(default=0)
    rn_total_activ = models.IntegerField(default=0)
    rn_half_life = models.IntegerField(default=0)
    rn_emission = models.CharField(max_length=50)

    # French radioactive waste parameters
    rn_vllw_class = models.IntegerField(default=0)
    rn_lma = models.IntegerField(default=0)
    rn_embed_limit = models.IntegerField(default=0)
    rn_iras = models.IntegerField(default=0)

    def __str__(self):
        return self.projects

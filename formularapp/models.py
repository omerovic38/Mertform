from django.db import models

# Create your models here.
class MultiStepFormModel(models.Model):
    id = models.AutoField(primary_key=True)
    privat_oder_gewerbe = models.CharField(max_length=255, default='-')
    strom_oder_gas = models.CharField(max_length=255, default='-', blank=True)
    personen_im_haushalt = models.CharField(max_length=255, default='-')
    wohnflaeche = models.CharField(max_length=255, default='-')
    gewerbeflaeche = models.CharField(max_length=255, default='-')
    grundversorger = models.CharField(max_length=255, default='-')
    oekotarif = models.CharField(max_length=255, default='-')
    plz=models.CharField(max_length=255, default='-')
    ort=models.CharField(max_length=255, default='-')
    rueckruftermin = models.CharField(max_length=255, default='-')
    nachricht=models.CharField(max_length=255)
#    objects=models.Manager()

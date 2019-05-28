from django.db import models

class Consumodeagua(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    Litros = models.FloatField(db_column='Litros', blank=True, null=True)  # Field name made lowercase.
    Fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConsumoDeAgua'


class Propiedades(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    Humedad = models.IntegerField(db_column='Humedad', blank=True, null=True)  # Field name made lowercase.
    Lluvia = models.IntegerField(db_column='Lluvia', blank=True, null=True)  # Field name made lowercase.
    Encendido = models.IntegerField(db_column='Encendido', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Propiedades'


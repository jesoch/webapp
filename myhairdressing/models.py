from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.


class Hairdressing(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    number = models.CharField(max_length=6)
    zipcode = models.CharField(max_length=6)
    city= models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    description = models.TextField(max_length=4000)
    schedule_hairdressing = models.CharField(max_length=70)
    image = models.FileField(upload_to='static/img')


    def __str__(self):
        return self.name


class Schedule(models.Model):

    id = models.AutoField(primary_key=True)
    DAY_CHOICES = ((1, 'Lunes'), (2, 'Martes'), (3, 'Miercoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sabado'))
    day = models.PositiveSmallIntegerField('Dia', blank=False, default=1, choices=DAY_CHOICES)
    HOUR_CHOICES = ((9, '09:00h'),(10, '10:00h'),(11, '11:00h'),(12, '12:00h'),(13, '13:00h'),(14, '14:00h'),(15, '15:00h'),
                    (16, '16:00h'),(17, '17:00h'),(18, '18:00h'),(19, '19:00h'),(20, '20:00h'),)
    hour = models.PositiveSmallIntegerField('Hora', blank=False, default=1, choices=HOUR_CHOICES)
    schedule_hairdressing = models.ForeignKey(Hairdressing, related_name='schedule')

class Citation(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User,related_name='citation')
    id_schedule = models.ForeignKey(Schedule, related_name='citation')

    def __str__(self):
        return 'Cita' + str(self.id)
from django.db import models

class HealthProgram(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    programs = models.ManyToManyField(HealthProgram, related_name='clients')

    def __str__(self):
        return self.name



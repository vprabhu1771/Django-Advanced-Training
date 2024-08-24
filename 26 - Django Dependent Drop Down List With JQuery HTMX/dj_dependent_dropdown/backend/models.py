from django.db import models


class Country(models.Model):

    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'country'


class State(models.Model):

    id = models.BigAutoField(primary_key=True)

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'state'

class City(models.Model):

    id = models.BigAutoField(primary_key=True)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'city'

class Person(models.Model):

    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=255)

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)

    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'person'
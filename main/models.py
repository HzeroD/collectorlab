from django.db import models
from django.shortcuts import render
from django.urls import reverse
from datetime import date


# Create your models here.
MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Animal(models.Model):
  name = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
      return self.name

  def get_absolute_url(self):
      return reverse('animals_detail', kwargs={'animal_id': self.id})


class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )
  animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

  def __str__(self):
    
     return f"{self.get_meal_display()} on {self.date}"

def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Meta:
    ordering = ['-date']





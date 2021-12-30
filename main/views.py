from django.shortcuts import render,redirect
from django.db import models
from .models import Animal
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')


def animals_index(request):
    animals = Animal.objects.all()
    return render(request, 'animals/index.html', {'animals':animals})

def animals_detail(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    feeding_form = FeedingForm()
    return render(request, 'animals/detail.html', {'animal':animal, 'feeding_form':feeding_form})

def add_feeding(request, animal_id):
    pass

def add_feeding(request, animal_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.animal_id = animal_id
    new_feeding.save()
  return redirect('animals_detail', animal_id=animal_id)

class AnimalCreate(CreateView):
    model = Animal
    fields = '__all__'
    success_url = '/cats/'

class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['name','color','description','age']

class AnimalDelete(DeleteView):
    model = Animal
    success_url='/animals/'






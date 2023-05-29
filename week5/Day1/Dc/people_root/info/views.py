from django.shortcuts import render
from .models import Post


people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

def people_list (request):
    sorted_people = sorted(people, key=lambda person: person['age'])
    context = {'people' : sorted_people}
    return render(request, 'people.html', context)

def person(request, id:int):
    person = None
    for i in people:
        if i['id'] == id:
            person = i
            break
    context = {'person_instance': person}
    return render(request, 'person.html', context)













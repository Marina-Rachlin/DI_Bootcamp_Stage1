from django.shortcuts import render
from .models import Person


def by_name(request, name_search: str):
    print("SEARCH", name_search)
    person = Person.objects.get(name=name_search)
    context={'person': person}
    return render(request, 'search.html', context)


def by_phone(request, phonenumber: str):
    print("SEARCH", phonenumber)
    person = Person.objects.get(phone_number=phonenumber)
    context={'person': person}
    return render(request, 'phone_search.html', context)


  
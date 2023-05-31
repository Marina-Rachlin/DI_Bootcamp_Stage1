from django.shortcuts import render
from .models import Person


def by_name(request, name_search: str):
    print("SEARCH", name_search)
    person = Person.objects.get(name=name_search)
    context={'person': person}
    return render(request, 'search.html', context)


def by_phone(request, phonenumber: str):
    print("SEARCH", phonenumber)
    person = None
    try:
        person = Person.objects.get(phone_number=phonenumber)
    except Person.DoesNotExist:
        pass
    context={'person': person}
    return render(request, 'phone_search.html', context)

from django.shortcuts import render, redirect
from .models import Person

def search_form(request):
    if request.method == 'POST':
        search_type = request.POST.get('search_type')
        search_query = request.POST.get('search_query')

        if search_type == 'phonenumber':
            return redirect('search_by_phonenumber', phonenumber=search_query)
        elif search_type == 'name':
            return redirect('search_by_name', name=search_query)

    return render(request, 'search_form.html')



  
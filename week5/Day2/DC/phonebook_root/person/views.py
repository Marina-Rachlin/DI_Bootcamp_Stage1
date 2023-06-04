from django.shortcuts import render,redirect
from .models import Person
from .forms import PhoneForm

def search_phone(request):
    
    if request.method == 'POST':
        query = request.POST['search']

        if PhoneForm({'number' : query}).is_valid():
            return redirect('phone', number = query)
        else:
            return redirect('name', input_name = query)

    return render(request, 'search-phone.html')
    

def phonenumber(request, number):

    try:
        person = Person.objects.get(phone_number = number)
    except Person.DoesNotExist:
        person = None

    context = {
        'person' : person
    }

    return render(request, 'number.html', context)


def name(request, input_name):
    try: 
        person = Person.objects.get(name = input_name)
    except Person.DoesNotExist:
        person = None

    context = {
        'person' : person
    }

    return render(request, 'name.html', context)

  
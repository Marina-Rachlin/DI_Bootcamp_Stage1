from django.shortcuts import render
import json


def read_data():
    filename = 'data.json'

    with open(filename, 'r') as file:
        data = json.load(file)

    return data

def animals_list(request):

    data = read_data()
    context = {'animals': data['animals']}

    return render (request,'animals.html',context)

def families_list(request):

    data = read_data()
    context = {'families': data['families']}

    return render(request, 'families.html', context)

def animal(request, id:int):
    data = read_data()
    animal = None
    for a in data['animals']:
        if a['id'] == id:
            animal = a
            break
    if not animal:
        pass

    return render(request, 'animal.html', {'animal': animal})

def family(request,id:int):
    data = read_data()
    family = None
    animals = []
    for f in data['families']:
        if f['id'] == id:
            family = f
            break
    if not family:
        pass
    else:
        for animal in data['animals']:
            if animal['family'] == id:
                animals.append(animal)
    return render(request, 'family.html', {'family': family, 'animals': animals})


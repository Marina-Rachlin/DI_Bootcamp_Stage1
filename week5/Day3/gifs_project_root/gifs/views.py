from django.shortcuts import redirect, render
from .forms import GifForm, CategoryForm
from .models import Gif, Category

def homepage(request):
    gifs = Gif.objects.all()
    for gif in gifs:
        print (gif.url)
    return render(request, 'homepage.html', {'gifs': gifs})


def add_new_gif(request):
    if request.method == 'POST':
        form = GifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = GifForm()
    return render(request, 'add_new_gif.html', {'form': form})


def add_new_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    form = CategoryForm()
    return render(request, 'add_new_category.html', {'form': form})

















# def category_view(request, category_id):
#     category = get_object_or_404(Category, id=category_id)
#     gifs = category.gifs.all()
#     return render(request, 'category_view.html', {'category': category, 'gifs': gifs})

# def categories_view(request):
#     categories = Category.objects.all()
#     return render(request, 'categories_view.html', {'categories': categories})

# def gif_view(request, gif_id):
#     gif = get_object_or_404(Gif, id=gif_id)
#     return render(request, 'gif_view.html', {'gif': gif})


from django.shortcuts import redirect, render
from .models import *
from .forms import CategoryForm, PostForm

# Create your views here.

def profile(request):
    current_user = Person.objects.get(first_name='John')
    addresses = current_user.addresses.all()

    user_email = current_user.email

    context ={'user': current_user, 'email': user_email, 'addresses': addresses}

    return render(request, 'profile.html',context)

def add_category_view(request):
    if request.method == 'POST':
        data = request.POST
        filled_form = CategoryForm(data)
        filled_form.save()
        print('Posting!')

    #GET
    category_form = CategoryForm(initial={'name': 'jbn'})
    context = {'form': category_form}
    return render (request, 'add_category.html', context)

def posts(request):
    posts_all = Post.objects.all()
    context = {'post_list': posts_all}
    return render(request, 'posts.html', context)

def add_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

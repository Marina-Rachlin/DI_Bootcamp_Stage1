from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Image, Profile

@login_required
def upload_image(request):
    if request.method == 'POST':
        # Process the uploaded image and save it to the Image model
        image_file = request.FILES['image']
        title = request.POST['title']
        description = request.POST['description']
        Image.objects.create(user=request.user, image_file=image_file, title=title, description=description)
        return redirect('image_list')
    return render(request, 'upload_image.html')

@login_required
def image_list(request):
    images = Image.objects.all()
    return render(request, 'image_list.html', {'images': images})


@login_required
def my_images(request):
    images = Image.objects.filter(user=request.user)
    return render(request, 'my_images.html', {'images': images})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('image_list')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    return render(request, 'profile.html', {'profile': profile})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})




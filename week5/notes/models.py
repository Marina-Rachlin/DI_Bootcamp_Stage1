from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

class Category(models.Model):
    name = models.CharField(max_length=20)


# python manage.py makemigrations - commit changes 
# python manage.py migrate - push changes


# -------------SINGLE INSTANCE-------------
# from polls.models import Post
# post1 = Post(title='First Post', content='test content', author='Joe')
# post1.save()
# post1.title = '1st Post'
# post1.delete()

# -------------Multiple INSTANCES-------------
# Post.objects.all() - returns all rows/objects
# Post.objects.last() - returns the last object
# Post.objects.first() - returns the first object

# Post.objects.all().order_by('author')

# get
# Post.objects.get(author='Adam') - returns single object

# filter
# Post.objects.filter(author='Joe') - returns multiple objects

# --------------Related model creation-----------
# category_science = Category(name='Science')
# category_science.save()
# post_science = Post(title='Mars', content='bla bla', author='Ben', category=category_science)
# post_science.save()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'phonebook',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR / "static")
]

# Media files (Uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = Path(BASE_DIR / 'media')

class Category(models.Model):
    name = models.CharField(max_length=20)


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
            return render(request, 'image_share/login.html', {'error_message': error_message})
    return render(request, 'image_share/login.html')




     # path('rental/add/', RentalCreateView.as_view(), name='rental_add'),
    # path('customer/', CustomerListView.as_view(), name='customer_list'),
    # path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    # path('customer/add/', CustomerCreateView.as_view(), name='customer_add'),
    # path('vehicle/', VehicleListView.as_view(), name='vehicle_list'),
    # path('vehicle/<int:pk>/', VehicleDetailView.as_view(), name='vehicle_detail'),
    # path('vehicle/add/', VehicleCreateView.as_view(), name='vehicle_add'),

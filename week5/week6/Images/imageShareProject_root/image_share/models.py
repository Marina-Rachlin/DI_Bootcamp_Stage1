from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Image(models.Model):
    image_file = models.ImageField(upload_to='image_files/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return {{self.title}}


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uploaded_images = models.IntegerField(default=0)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Image)
def update_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = instance.user.profile
        user_profile.uploaded_images = Image.objects.filter(user=instance.user).count()
        user_profile.save()        



    
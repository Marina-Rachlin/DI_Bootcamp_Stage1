# Generated by Django 4.2.2 on 2023-06-20 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0003_category_upcomingevents_roomamenities_room_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomamenities',
            name='category',
        ),
        migrations.AddField(
            model_name='roomamenities',
            name='categories',
            field=models.ManyToManyField(to='visitors.category'),
        ),
    ]

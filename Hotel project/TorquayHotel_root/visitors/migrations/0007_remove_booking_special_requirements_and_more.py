# Generated by Django 4.2.2 on 2023-06-22 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0006_guestdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='special_requirements',
        ),
        migrations.AddField(
            model_name='booking',
            name='guest_details',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='visitors.guestdetails'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='payment_status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Pending', 'Pending')], default='Pending', max_length=20),
        ),
    ]
# Generated by Django 4.2.7 on 2024-01-15 03:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('slug', models.SlugField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Specialisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('slug', models.SlugField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.IntegerField()),
                ('meet', models.CharField(max_length=100)),
                ('imgage', models.ImageField(upload_to='doctor/images/')),
                ('available_time', models.ManyToManyField(to='doctor.availabletime')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.designation')),
                ('specialisation', models.ManyToManyField(to='doctor.specialisation')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

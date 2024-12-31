# Generated by Django 5.1.4 on 2024-12-30 23:54

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CampusStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=67, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='VoxotronForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter', models.CharField(max_length=67)),
                ('vote_date', models.DateTimeField(default=datetime.datetime.now)),
                ('vote', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.campusstudent')),
            ],
        ),
    ]
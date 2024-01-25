# Generated by Django 4.2.7 on 2024-01-23 06:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0001_initial'),
        ('train', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddTrain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('total_number_of_seats', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(999)])),
                ('train_date', models.CharField(max_length=50)),
                ('end_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='end_trains', to='station.station')),
                ('start_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_trains', to='station.station')),
            ],
        ),
    ]

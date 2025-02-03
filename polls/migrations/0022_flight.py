# Generated by Django 5.1.4 on 2025-01-30 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_remove_hotel_star'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=100)),
                ('departure', models.CharField(max_length=100)),
                ('arrival', models.CharField(max_length=100)),
                ('departure_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]

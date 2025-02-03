# Generated by Django 5.1.4 on 2025-01-30 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_flight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('nombre_de_personnes', models.IntegerField()),
                ('compagnie', models.CharField(max_length=100)),
                ('depart', models.CharField(max_length=100)),
                ('arrivee', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type_vol', models.CharField(max_length=50)),
                ('classe', models.CharField(max_length=50)),
            ],
        ),
    ]

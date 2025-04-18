# Generated by Django 5.1.4 on 2025-01-31 01:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_reserver_vol_delete_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('telephone', models.CharField(max_length=20, verbose_name='Téléphone')),
                ('passeport', models.CharField(max_length=50, verbose_name='Passeport')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compagnie', models.CharField(max_length=100, verbose_name='Compagnie')),
                ('depart', models.CharField(max_length=100, verbose_name='Départ')),
                ('arrivee', models.CharField(max_length=100, verbose_name='Arrivée')),
                ('date', models.DateField(verbose_name='Date')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Prix')),
                ('type_vol', models.CharField(choices=[('Aller-Retour', 'Aller-Retour'), ('Aller-simple', 'Aller-simple')], max_length=50, verbose_name='Type de vol')),
                ('classe', models.CharField(choices=[('Economique', 'Economique'), ('Eco Premium', 'Eco Premium'), ('Affaires', 'Affaires'), ('Première', 'Première')], max_length=50, verbose_name='Classe')),
                ('nombre_de_personnes', models.IntegerField(verbose_name='Nombre de personnes')),
            ],
        ),
        migrations.DeleteModel(
            name='reserver_vol',
        ),
        migrations.AddField(
            model_name='passager',
            name='reservation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passagers', to='polls.reservation'),
        ),
    ]

# Generated by Django 5.1.4 on 2025-01-28 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_hotel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='star',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

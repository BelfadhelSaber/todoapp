# Generated by Django 5.1.4 on 2025-01-26 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_delete_vol_hotel_select'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='select',
        ),
    ]

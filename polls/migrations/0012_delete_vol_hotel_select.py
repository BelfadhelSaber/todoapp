<<<<<<< HEAD
# Generated by Django 5.1.4 on 2025-01-26 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_remove_vol_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vol',
        ),
        migrations.AddField(
            model_name='hotel',
            name='select',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
=======
# Generated by Django 5.1.4 on 2025-01-26 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_remove_vol_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vol',
        ),
        migrations.AddField(
            model_name='hotel',
            name='select',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
>>>>>>> master

# Generated by Django 2.2.7 on 2019-12-07 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0005_auto_20191204_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='Date',
            field=models.DateField(),
        ),
    ]

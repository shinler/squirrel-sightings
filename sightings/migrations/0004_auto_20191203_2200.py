# Generated by Django 2.2.7 on 2019-12-03 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0003_auto_20191203_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='Date',
            field=models.DateTimeField(),
        ),
    ]

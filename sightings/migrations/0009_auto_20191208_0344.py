# Generated by Django 2.2.7 on 2019-12-08 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0008_auto_20191208_0323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sighting',
            name='id',
        ),
        migrations.AlterField(
            model_name='sighting',
            name='unique_squirrel_id',
            field=models.CharField(help_text='unique squirrel id', max_length=100, primary_key=True, serialize=False),
        ),
    ]

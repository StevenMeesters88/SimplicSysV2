# Generated by Django 4.2.1 on 2023-06-04 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0005_servicemodel_way_of_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetypemodel',
            name='sort_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='servicetypemodel',
            name='visa_hemsida',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0007_servicemodel_service_protocol'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicemodel',
            name='service_protocol_available',
            field=models.BooleanField(default=False),
        ),
    ]

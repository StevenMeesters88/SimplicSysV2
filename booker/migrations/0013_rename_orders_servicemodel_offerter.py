# Generated by Django 4.2.1 on 2023-06-05 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0012_alter_contactmodel_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicemodel',
            old_name='orders',
            new_name='offerter',
        ),
    ]

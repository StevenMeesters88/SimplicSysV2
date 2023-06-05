# Generated by Django 4.1.4 on 2023-03-31 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerter', '0002_standardoffert_pris_ex_moms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardoffert',
            name='momstotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='standardoffert',
            name='pris_ex_moms',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='standardoffert',
            name='totalpris',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
    ]
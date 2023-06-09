# Generated by Django 4.2.1 on 2023-06-05 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0010_contactmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('betalstatus', models.CharField(choices=[('Obetalt', 'Obetalt'), ('Swish', 'Swish'), ('Kort', 'Kort'), ('Kontant', 'Kontant'), ('Annat, se notering', 'Annat, se notering')], default='Obetalt', max_length=25)),
                ('notes', models.TextField()),
                ('regnr', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='booker.customermodel')),
                ('service_date', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='booker.servicemodel')),
            ],
        ),
    ]

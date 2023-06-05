from django.db import models


# Create your models here.
class StandardOffert(models.Model):
    offert = models.AutoField(primary_key=True)
    regnr = models.CharField(max_length=255)
    pris_ex_moms = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    momstotal = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    totalpris = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    giltigt_tom = models.DateField()    # default=(date.today() + timedelta(days=90)))
    noteringar = models.TextField(default='')

    class Meta:
        verbose_name = 'Offerter'
        verbose_name_plural = 'Offerter'


class OffertPost(models.Model):
    offert = models.ForeignKey(StandardOffert, on_delete=models.CASCADE)
    produkt = models.CharField(max_length=255)
    pris = models.DecimalField(default=0.00, decimal_places=2, max_digits=6)
    moms = models.DecimalField(default=0.25, decimal_places=2, max_digits=6)
    totalpris = models.DecimalField(default=0.00, decimal_places=2, max_digits=6)

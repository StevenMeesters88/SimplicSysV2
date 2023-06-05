import datetime

from django.db import models

# OneToOneField -> OneToOneRel
# ForeignKey -> ManyToOneRel
# ManyToManyField -> ManyToManyRel


class ServiceTypeModel(models.Model):
    sort_id = models.IntegerField(default=1)
    service_name = models.CharField(max_length=255)
    service_price = models.DecimalField(default=0.00, max_digits=20, decimal_places=0)
    service_description = models.TextField()
    image = models.ImageField(upload_to='media/')
    visa_hemsida = models.BooleanField(default=False)

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = 'Våra servicar'
        verbose_name_plural = 'Våra servicar'


class CustomerModel(models.Model):
    regnr = models.CharField(max_length=6, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    telefon = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    notering = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.regnr

    class Meta:
        verbose_name = 'Kunder'
        verbose_name_plural = 'Kunder'


class ServiceModel(models.Model):

    STATUS_CHOICES = (
        ('Bokad', 'Bokad'),
        ('Beställning pågår', 'Beställning pågår'),
        ('Utförd', 'Utförd'),
        ('Avbokad', 'Avbokad')
    )

    WAY_BOOKED_CHOICES = (
        ('', ''),
        ('Inloggad', 'Inloggad'),
        ('Utloggad', 'Utloggad'),
        ('Telefon', 'Telefon'),
        ('Email', 'Email'),
        ('Verkstad', 'Verkstad')
    )

    regnr = models.ForeignKey(CustomerModel, on_delete=models.PROTECT)
    booked_date = models.DateTimeField(auto_now=True)
    service_type = models.ForeignKey(ServiceTypeModel, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Bokad')
    notes = models.TextField()
    service_date = models.DateTimeField()
    offerter = models.CharField(max_length=255, default='')
    way_of_booking = models.CharField(max_length=20, choices=WAY_BOOKED_CHOICES, default='')
    service_protocol_available = models.BooleanField(default=False)
    service_protocol = models.FileField(upload_to='media/protocols/')

    # def __str__(self):
    #     return datetime.datetime.strptime(self.booked_date, '%Y-%m-%d %H:%M').strftime('%Y-%m-%d %H:%M')

    class Meta:
        verbose_name = 'Bokningar'
        verbose_name_plural = 'Bokningar'


class ContactModel(models.Model):

    STATUS_OPTIONS = (
        ('Oläst', 'Oläst'),
        ('I behandling', 'I behandling'),
        ('Väntar på kund', 'Väntar på kund'),
        ('Beställt delar', 'Beställt delar'),
        ('Klart', 'Klart')
    )

    inkommen = models.DateTimeField(auto_now=True)
    namn = models.CharField(max_length=255)
    regnr = models.CharField(max_length=255)
    telnr = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    meddelande = models.TextField(blank=True, null=True)
    action = models.TextField(default='', blank=True)
    klart = models.CharField(max_length=15, choices=STATUS_OPTIONS, default='Oläst')

    class Meta:
        verbose_name = 'Kundkontakter'
        verbose_name_plural = 'Kundkontakter'


class PaymentsModel(models.Model):
    PAYMENT_CHOICES = (
        ('Obetalt', 'Obetalt'),
        ('Swish', 'Swish'),
        ('Kort', 'Kort'),
        ('Kontant', 'Kontant'),
        ('Annat, se notering', 'Annat, se notering')
    )

    regnr = models.ForeignKey(CustomerModel, on_delete=models.PROTECT)
    service_date = models.ForeignKey(ServiceModel, on_delete=models.PROTECT)
    betalstatus = models.CharField(max_length=25, default='Obetalt', choices=PAYMENT_CHOICES)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Betalningar'
        verbose_name_plural = 'Betalningar'

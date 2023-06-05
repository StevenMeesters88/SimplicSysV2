from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import models
from . import forms
import operator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from . import models
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def homepage(request):
    return render(request, 'home.html')


def boka(request):

    services = models.ServiceTypeModel.objects.filter(~Q(visa_hemsida=False))
    ordered = sorted(services, key=operator.attrgetter('sort_id'))

    return render(request, 'boka.html', context={'data': ordered})


def om_oss(request):

    if request.user.is_authenticated:
        logged_in_user = request.user
        user_data = User.objects.get(username=logged_in_user.username)
        first_name = user_data.first_name

    else:
        first_name = ''

    return render(request, 'om_oss.html', context={'first_name': first_name})


def kontakt(request):

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = forms.KontaktLoggedIn(request.POST)
            if form.is_valid():
                logged_in_user = request.user
                user_data = User.objects.get(username=logged_in_user.username)
                contact = models.ContactModel(namn=f'{user_data.first_name} {user_data.last_name}',
                                         regnr=user_data.username,
                                         telnr='TO BE IMPLEMENTED',
                                         email=user_data.email,
                                         meddelande=form.cleaned_data['meddelande'])
                contact.save()

                x = 0

                return render(request, 'tackmeddelande.html', context={'x': x, 'first_name': user_data.first_name})
        else:
            form = forms.KontaktLoggedOut(request.POST)
            if form.is_valid():
                contact = models.ContactModel(namn=form.cleaned_data['namn'],
                                              regnr=form.cleaned_data['regnr'],
                                              telnr=form.cleaned_data['phone'],
                                              email=form.cleaned_data['email'],
                                              meddelande=form.cleaned_data['meddelande'])
                name = form.cleaned_data['namn']
                contact.save()

                x = 1

                return render(request, 'tackmeddelande.html', context={'x': x, 'first_name': name})

    else:
        if request.user.is_authenticated:
            form = forms.KontaktLoggedIn()
            return render(request, 'kontakt.html', context={'form': form})
        else:
            form = forms.KontaktLoggedOut()
            return render(request, 'kontakt.html', context={'form': form})


    return render(request, 'kontakt.html')


def faq(request):
    return render(request, 'faq.html')


def skapakonto(request):

    if request.method == 'POST':
        form = forms.NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            new_user = User.objects.create_user(username, email, password)
            new_user.first_name = form.cleaned_data['first_name']
            first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.phone = form.cleaned_data['phone']     # to be fixed in db
            new_user.save()

            # Info skall mailas till kunden! to be fixed

            return render(request, 'kontoskapat.html', context={'name': first_name})

    else:
        form = forms.NewUserForm()

    return render(request, 'skapakonto.html', context={'form': form})


@login_required()
def min_profil(request):

    user = request.user
    print('username: ', user.username)

    mina_servicar = models.ServiceModel.objects.filter(regnr=f'{user.username}')
    # mina_servicar = list(mina_servicar)

    return render(request, 'min_profil.html', context={'user': user, 'mina_servicar': mina_servicar})


def boka_two(request, service_name=None):
    service_name = get_object_or_404(models.ServiceTypeModel, service_name=service_name)

    if request.method == 'POST':
        if request.user.is_authenticated:       # fetch customer data
            form = forms.BokaLoggedIn(request.POST)
            if form.is_valid():
                logged_in_user = request.user
                user_data = User.objects.get(username=logged_in_user.username)
                try:
                    cust_exists = models.CustomerModel.objects.get(regnr=logged_in_user.username)
                except ObjectDoesNotExist:
                    new_cst = models.CustomerModel(regnr=user_data.username,
                                                   first_name=user_data.first_name,
                                                   last_name=user_data.last_name,
                                                   email=user_data.email)
                    first_name = user_data.first_name
                    new_cst.save()
                finally:
                    reg = models.CustomerModel.objects.get(regnr=user_data.username)
                    new_serv = models.ServiceModel(regnr=reg,
                                                   service_type=service_name,
                                                   status='bokad',
                                                   notes=form.cleaned_data['notes'],
                                                   service_date=form.cleaned_data['service_date'],
                                                   way_of_booking='Inloggad')
                    new_serv.save()

                    resp_val = 0

                    return render(request, 'boka_confirm.html', context={'resp_val': resp_val, 'first_name': 'TO_BE_FIXED'})

        else:                                   # ask for all data
            form = forms.BokaLoggedOut(request.POST)
            if form.is_valid():
                regnr = form.cleaned_data['regnr']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']

                cust = models.CustomerModel(regnr=regnr,
                                            first_name=first_name,
                                            last_name=last_name,
                                            telefon=phone,
                                            email=email)
                cust.save()

                reg = models.CustomerModel.objects.get(regnr=regnr)
                serv = models.ServiceModel(regnr=reg,
                                           service_type=service_name,
                                           status='bokad',
                                           notes=form.cleaned_data['notes'],
                                           service_date=form.cleaned_data['service_date'],
                                           way_of_booking='Utloggad')
                serv.save()

                resp_val = 1

                return render(request, 'boka_confirm.html', context={'resp_val': resp_val, 'first_name': first_name})

    else:
        if request.user.is_authenticated:       # send empty form with reduced fields
            form = forms.BokaLoggedIn()
        else:                                   # send empty form with all fields
            form = forms.BokaLoggedOut()

    return render(request, 'boka_two.html', context={'form': form})

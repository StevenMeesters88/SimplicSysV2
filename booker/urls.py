from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('boka/', views.boka, name='boka'),
    path('boka_two/<str:service_name>', views.boka_two, name='boka_two'),
    path('om_oss/', views.om_oss, name='om_oss'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('faq/', views.faq, name='faq'),
    path('minprofil/', views.min_profil, name='minprofil'),
    path('skapakonto/', views.skapakonto, name='skapakonto')
]

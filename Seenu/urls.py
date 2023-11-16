from Seenu.views import *
from django.urls import path
app_name='Tour'
urlpatterns=[
    path('Seenu/',Seenu,name='Seenu')
]
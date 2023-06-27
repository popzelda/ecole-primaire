from django.urls import path
from .views import *


app_name="compte"

urlpatterns = [
    path('create/',create_compte,name='create_compte')
]

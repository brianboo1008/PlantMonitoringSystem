from django.urls import path
from . import views

urlpatterns = [
path('',views.dry),
path('rain/',views.rain),
path('data/',views.receivedata),
path('node/',views.updatenode),
]

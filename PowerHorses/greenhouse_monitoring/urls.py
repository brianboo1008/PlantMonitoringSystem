from django.urls import path
from . import views

urlpatterns = [
path('',views.temp),
path('humidity/',views.humid),
path('lightintensity/',views.light),
path('data/',views.receivedata),
path('node/',views.updatenode),
]

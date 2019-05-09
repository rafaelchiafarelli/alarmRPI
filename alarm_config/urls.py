from django.urls import path
from landpage.views import landpage,ContactInfo,home


urlpatterns = [
    path('', landpage, name='landpage'),
    path('contact/',ContactInfo, name="contact"),
    path('home/', home, name='home')
    ]
from django.urls import path

from recipes.views import about, contact, home

urlpatterns = [
    path('', home),  # HOME
    path('about/', about),  # /sobre/
    path('contact/', contact)  # /contato/
]

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('home/', home.site.urls), path('contato/', contato.site.urls),path('sobre/', sobre.site.urls),path('teste/', teste.site.urls),
]
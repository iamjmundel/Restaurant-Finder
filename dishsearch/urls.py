from django.contrib import admin
from django.urls import path
from dishsearchapp.views import search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search, name='search'),
]

from django.urls import include,path
from django.contrib import admin

from property import views

urlpatterns = [
    path('', views.show_flats, name='flats'),  # главная страница
    path('search/', views.show_flats, name='search_flats'),  # /search/
    path('admin/', admin.site.urls),  # админка
]

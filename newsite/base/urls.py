from django.urls import path

from . import views

urlpatterns = [
    path('time/', views.show_time),
    path('light/', views.light_page)
]

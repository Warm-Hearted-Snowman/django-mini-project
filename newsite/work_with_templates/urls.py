from django.urls import path
from . import views

urlpatterns = [
    path('usrs/', views.show_users)
]
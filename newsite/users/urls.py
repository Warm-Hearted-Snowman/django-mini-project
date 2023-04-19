from django.urls import path
from . import views

urlpatterns = [
    path('info/<int:user_id>/', views.show_infos, name='info'),
    path('all/', views.show_users, name='users'),
    path('delete/<int:user_id>', views.delete_user, name='delete'),
    path('create/', views.crate_user, name='create'),
    path('update/<int:user_id>/', views.update , name='update')
]

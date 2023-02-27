from django.urls import path
from . import views


urlpatterns = [
    path('', views.reservations, name='reservations'),
    path('', views.reserve_table, name='reserve_table'),
    path('<int:table_id>/', views.confirm_reservation, name='confirm_reservation'),
    path('table/<int:table_id>/reserve/', views.reserve_table, name='reserve_table'),
]

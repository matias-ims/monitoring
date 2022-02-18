from django.urls import path

from .views import dashboard, telemetria_data

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/data/', telemetria_data, name='telemetria_data')
]
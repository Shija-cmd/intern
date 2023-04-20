from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.data, name='dashboard-data'),
    path('predictions/', views.predictions, name='dashboard-predictions'),
]
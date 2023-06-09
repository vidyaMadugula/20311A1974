from django.urls import path
from number_management_app.views import get_numbers

urlpatterns = [
    path('numbers', get_numbers, name='get_numbers'),
]
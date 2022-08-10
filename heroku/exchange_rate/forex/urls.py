from django.urls import  path
from forex import views

urlpatterns = [
    path('rates/<str:date>', views.get_rates, name = "get_rates"),
]

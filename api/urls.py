from django.urls import path
from . import views

urlpatterns = [
    path('', views.ForecastingView.as_view())
]

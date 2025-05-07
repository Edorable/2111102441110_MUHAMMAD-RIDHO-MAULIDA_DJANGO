from django.urls import path
from news.views import dashboard

urlpatterns =   [
    path('', dashboard, name="dashboard"),
]
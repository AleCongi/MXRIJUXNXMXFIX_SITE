from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # Altre URL e viste se necessario
]

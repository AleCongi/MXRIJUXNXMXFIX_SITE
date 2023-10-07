from django.urls import path
from . import views, admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    # Altre URL e viste se necessario
]

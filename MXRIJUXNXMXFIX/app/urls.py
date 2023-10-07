from django.urls import path
from django.contrib import admin

from . import views

import logging


logger = logging.getLogger("aled")

logger.info(admin)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    # Altre URL e viste se necessario
]

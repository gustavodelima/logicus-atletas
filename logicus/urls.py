from django.contrib import admin
from django.urls import path, include
from django_prometheus import exports


admin.site.site_header = "Logicus Esportes"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('atletas.urls')),
    path('', include('django_prometheus.urls')),
    # path('', include('admin_berry.urls')),
]

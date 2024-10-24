from django.contrib import admin
from django.urls import path, include
from accounts import views  # Importa las vistas de tu aplicación

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.home_view, name='home'),  # Asegúrate de que 'home_view' esté definido en 'myapp/views.py'
]

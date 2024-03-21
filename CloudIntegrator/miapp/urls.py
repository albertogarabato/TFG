from django.urls import path
from . import views

urlpatterns = [
    # URL para la página de inicio
    path('', views.index, name='index'),

    # URL para la página "Acerca de"
    path('about/', views.about, name='about'),

    # URL para la página de contacto
    path('contacto/', views.contacto, name='contacto'),

    # URL para la vista de validación y conexión a la base de datos
    path('validate_and_connect/', views.validate_and_connect, name='validate_and_connect'),
]

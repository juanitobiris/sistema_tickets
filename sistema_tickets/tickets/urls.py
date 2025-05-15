from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tickets, name='lista_tickets'),
    path('nuevo/', views.crear_ticket, name='crear_ticket'),
    path('<int:ticket_id>/', views.detalle_ticket, name='detalle_ticket'),
    path('<int:ticket_id>/editar/', views.editar_ticket, name='editar_ticket'),
    path('<int:ticket_id>/eliminar/', views.eliminar_ticket, name='eliminar_ticket'),
]
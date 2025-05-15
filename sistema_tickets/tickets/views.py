from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_tickets(request):
    tickets = Ticket.objects.all().order_by('-creado_en')
    return render(request, 'tickets/lista_tickets.html', {'tickets': tickets})

@login_required
def crear_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.creado_por = request.user
            ticket.save()
            return redirect('lista_tickets')
    else:
        form = TicketForm()
    return render(request, 'tickets/crear_ticket.html', {'form': form})

from django.shortcuts import get_object_or_404

@login_required
def detalle_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, 'tickets/detalle_ticket.html', {'ticket': ticket})

    from django.http import HttpResponseForbidden

@login_required
def editar_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.user != ticket.creado_por and not request.user.is_superuser:
        return HttpResponseForbidden("No tienes permiso para editar este ticket.")

    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('detalle_ticket', ticket_id=ticket.id)
    else:
        form = TicketForm(instance=ticket)

    return render(request, 'tickets/editar_ticket.html', {'form': form, 'ticket': ticket})

@login_required
def eliminar_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.user != ticket.creado_por and not request.user.is_superuser:
        return HttpResponseForbidden("No tienes permiso para eliminar este ticket.")

    if request.method == 'POST':
        ticket.delete()
        return redirect('lista_tickets')

    return render(request, 'tickets/eliminar_ticket.html', {'ticket': ticket})
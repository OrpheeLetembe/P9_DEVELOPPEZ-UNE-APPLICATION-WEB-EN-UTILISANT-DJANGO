from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import forms


@login_required
def flux_page(request):
    return render(request, 'blog/flux.html')


def create_ticket(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.Post, request.Files)
        ticket = form.save(commit=False)
        ticket.user = request.user
        ticket.save()

    return render(request, 'blog/create_ticket.html', context={'form': form})

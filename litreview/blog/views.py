from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import forms
from blog.models import Ticket
from authentication.models import User


@login_required
def flux_page(request):
    user = User.objects.all()
    return render(request, 'blog/flux.html')


@login_required
def post_page(request):
    tickets = Ticket.objects.all()
    return render(request, 'blog/post.html', context={'tickets': tickets})


@login_required
def subscript_page(request):
    users = User.objects.all()
    return render(request, 'blog/subscrip.html', context={'users': users})


@login_required
def create_review(request):
    return render(request, 'blog/review.html')


@login_required
def create_ticket(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('flux')
    return render(request, 'blog/create_ticket.html', context={'form': form})


@login_required
def create_review(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('flux')
    context = {
            'ticket_form': ticket_form,
            'review_form': review_form,
        }
    return render(request, 'blog/review.html', context=context)

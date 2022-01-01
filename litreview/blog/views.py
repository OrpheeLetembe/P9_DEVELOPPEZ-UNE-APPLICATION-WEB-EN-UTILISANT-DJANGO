from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import forms


@login_required
def flux_page(request):
    return render(request, 'blog/flux.html')


@login_required
def post_page(request):
    return render(request, 'blog/post.html')


@login_required
def subscript_page(request):
    return render(request, 'blog/subscrip.html')


@login_required
def create_review(request):
    return render(request,'blog/review.html')


@login_required
def create_ticket(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.Post, request.Files)
        ticket = form.save(commit=False)
        ticket.user = request.user
        ticket.save()

    return render(request, 'blog/create_ticket.html', context={'form': form})

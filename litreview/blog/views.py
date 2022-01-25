from itertools import chain
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from authentication.models import User
from blog import forms
from blog.models import UserFollows, Review, Ticket


@login_required
def flux_page(request):
    followed_users = [x.followed_user for x in UserFollows.objects.filter(user=request.user)]
    tickets = Ticket.objects.filter(Q(user__in=followed_users) | Q(user=request.user))
    reviews = Review.objects.filter(Q(user__in=followed_users) | Q(user=request.user) | Q(ticket__user=request.user))

    reviews_and_tickets = sorted(
        chain(reviews, tickets),
        key=lambda instance: instance.time_created,
        reverse=True
    )
    paginator = Paginator(reviews_and_tickets, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'blog/flux.html', context=context)


@login_required
def post_page(request):
    reviews = Review.objects.filter(user=request.user)
    tickets = Ticket.objects.filter(user=request.user)

    reviews_and_tickets = sorted(
        chain(reviews, tickets),
        key=lambda instance: instance.time_created,
        reverse=True
    )

    paginator = Paginator(reviews_and_tickets, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'blog/post.html', context=context)


@login_required
def ticket_update(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = forms.TicketForm(instance=ticket)
    context = {
        'form': form,
        'ticket': ticket,
    }
    return render(request, 'blog/ticket_update.html', context=context)


@login_required
def ticket_delete(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('post')
    return render(request, 'blog/ticket_delete.html', context={'ticket': ticket})


@login_required
def review_update(request, review_id):
    review = Review.objects.get(id=review_id)
    ticket = review.ticket
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = forms.ReviewForm(instance=review)

    context = {
        'form': form,
        'ticket': ticket,

    }
    return render(request, 'blog/review_update.html', context=context)


@login_required
def review_delete(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('post')
    return render(request, 'blog/review_delete.html', context={'review': review})


@login_required
def subscript_page(request):
    message = ""
    form = forms.UserFollowing()
    followed_users = [x.followed_user for x in UserFollows.objects.filter(user=request.user)]
    followers = [x.user for x in UserFollows.objects.filter(followed_user=request.user)]

    if request.method == 'POST':
        form = forms.UserFollowing(request.POST)
        if form.is_valid():
            followed_user_id = form.cleaned_data.get("followed_user")
            try:
                followed_user = User.objects.get_by_natural_key(followed_user_id)
            except User.DoesNotExist as e:
                e = "Cet utilisateur n'existe pas"
                context = {
                    'form': form,
                    'followed_users': followed_users,
                    'followers': followers,
                    'user': request.user,
                    "error": e
                }

                return render(request, 'blog/subscrip.html', context=context)
            if followed_user in followed_users:
                message = "Cet utilisateur est déja suivi."
                context = {
                    'form': form,
                    'followed_users': followed_users,
                    'followers': followers,
                    'user': request.user,
                    "message": message
                }
                return render(request, 'blog/subscrip.html', context=context)
            elif followed_user == request.user:
                message = "Vous ne pouvez pas vous suivre."

                context = {
                    'form': form,
                    'followed_users': followed_users,
                    'followers': followers,
                    'user': request.user,
                    "message": message
                }
                return render(request, 'blog/subscrip.html', context=context)

            else:
                UserFollows(
                    followed_user=followed_user, user=request.user).save()
            return redirect('subscrip')
    context = {
            'form': form,
            'followed_users': followed_users,
            'followers': followers,
            'user': request.user,
            'message': message
        }
    return render(request, 'blog/subscrip.html', context=context)


@login_required
def follow_delete(request, user_id):
    follow = UserFollows.objects.get(Q(followed_user=user_id) & Q(user=request.user))
    if request.method == 'POST':
        follow.delete()
        return redirect('subscrip')
    return render(request, 'blog/follow_remove.html', context={'follow': follow})


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
    context = {
        'form': form,
        'user': request.user,
    }
    return render(request, 'blog/create_ticket.html', context=context)


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
            'user': request.user,
    }
    return render(request, 'blog/review.html', context=context)


@login_required
def review_answer(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('flux')
    context = {
        'ticket': ticket,
        'review_form': review_form,
        'user': request.user
    }
    return render(request, 'blog/review_answer.html', context=context)

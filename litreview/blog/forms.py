from django import forms
from . import models


class TicketForm(forms.ModelForm):
    titre = forms.CharField(widget=forms.TextInput(attrs={"size": 100}))
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 10, "cols": 100}))

    class Meta:
        model = models.Ticket
        fields = ['titre', 'description', 'image']


class UserFollowing(forms.ModelForm):
    pass


class ReviewForm(forms.ModelForm):
    CHOICES = [
        (0, "0"),
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    ]
    headline = forms.CharField(label="Titre", widget=forms.TextInput(attrs={"size": 100}))
    rating = forms.ChoiceField(label='Note', choices=CHOICES, widget=forms.RadioSelect())

    body = forms.CharField(label='Commentaire', widget=forms.Textarea)

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']

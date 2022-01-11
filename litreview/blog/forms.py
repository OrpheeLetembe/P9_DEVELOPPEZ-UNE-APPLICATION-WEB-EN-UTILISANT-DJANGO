from django import forms
from . import models


class TicketForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"size": 100, "placeholder": "Titre"}))
    description = forms.CharField(label="", widget=forms.Textarea(attrs={"rows": 10, "cols": 101,
                                                                         "placeholder": "Description"}))
    image = forms.ImageField(label="", widget=forms.FileInput(attrs={'placeholder': 'im'}))

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class UserFollowing(forms.ModelForm):
    followed_user = forms.CharField(label="", widget=forms.TextInput(attrs={"size": 80,
                                                                            "placeholder": "Nom d'utilisateur"}))

    class Meta:
        model = models.UserFollows
        fields = ['followed_user']


class ReviewForm(forms.ModelForm):
    CHOICES = [
        (0, "0"),
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    ]
    headline = forms.CharField(label='Titre', widget=forms.TextInput(attrs={"size": 100}))
    rating = forms.ChoiceField(label='Note', choices=CHOICES, widget=forms.RadioSelect())

    body = forms.CharField(label='Commentaire', widget=forms.Textarea)

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']

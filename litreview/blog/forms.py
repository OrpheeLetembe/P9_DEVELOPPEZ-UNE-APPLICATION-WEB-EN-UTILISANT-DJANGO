from django import forms
from . import models


class TicketForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"size": 80, "placeholder": "Titre"}))
    description = forms.CharField(label="", widget=forms.Textarea(attrs={"rows": 5, "cols": 81,
                                                                         "placeholder": "Description"}))
    image = forms.ImageField(label="", widget=forms.FileInput())

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class UserFollowing(forms.Form):
    followed_user = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'text-center',
                                                                            "size": 50,
                                                                            "placeholder": "Nom d'utilisateur"}))


class ReviewForm(forms.ModelForm):
    CHOICES = [
        (0, "0"),
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    ]
    headline = forms.CharField(label='', widget=forms.TextInput(attrs={"size": 80, "placeholder": "Titre"}))
    rating = forms.ChoiceField(label='Note', choices=CHOICES, widget=forms.RadioSelect())

    body = forms.CharField(label='', widget=forms.Textarea(attrs={"rows": 5, "cols": 81, "placeholder": "commentaire"}))

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']

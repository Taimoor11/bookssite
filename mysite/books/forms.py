from django import forms
from .models import Comment,Books,Publisher,Author,Category, RATING_CHOICES


class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class MovieFilterForm(forms.Form):
    category = forms.ModelChoiceField(
        label="Category",
        required=False,
        queryset=Category.objects.all())
    publisher = forms.ModelChoiceField(
        label="Publisher",
        required=False,
        queryset=Publisher.objects.all())
    author = forms.ModelChoiceField(
        label="Author",
        required=False,
        queryset=Author.objects.all())
    rating = forms.ChoiceField(
        label="Rating",
        required=False,
        choices=RATING_CHOICES)
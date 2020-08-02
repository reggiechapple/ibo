from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Professional
from users.models import User


class ProfessionalSignUpForm(UserCreationForm):
    email = forms.CharField(min_length=1, max_length=60, widget=forms.EmailInput(
        attrs={'class': '', 'placeholder': 'Email'}))
    name = forms.CharField(min_length=1, max_length=60, widget=forms.TextInput(
        attrs={'class': '', 'placeholder': 'Name'}))
    photo = forms.ImageField(widget=forms.FileInput(
        attrs={'class': ''}))
    password1 = forms.CharField(min_length=1, max_length=60, widget=forms.PasswordInput(
        attrs={'class': '', 'placeholder': 'Password'}))
    password2 = forms.CharField(min_length=1, max_length=60, widget=forms.PasswordInput(
        attrs={'class': '', 'placeholder': 'Confirm Password'}))

    class Meta(UserCreationForm):
        model = User
        fields = ('name', 'email', 'photo',)

    def save(self):
        user = super().save(commit=False)
        user.is_professional = True
        user.save()
        Professional.objects.create(user=user)
        return user
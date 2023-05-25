from django.shortcuts import render
from .forms import MyUserCreationForm, User
from django.views.generic import CreateView
from django.urls import reverse_lazy


class RegisterView(CreateView):
    model = User
    form_class = MyUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'auth_app/register.html'




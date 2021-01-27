from django.shortcuts import render
from django.urls import reverse_lazy
# reverse_lazy can help us where to navigate the user once they signup/login
from django.views.generic import CreateView

from . import forms


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

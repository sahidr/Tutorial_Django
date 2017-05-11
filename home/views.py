from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import User
from .forms import UserForm
from django.http import JsonResponse


class Home (TemplateView):
    template_name = 'home/home.html'


class List (TemplateView):
    template_name = 'home/user_list.html'

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        context['first_name'] = User.objects.all()
        return context


def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'home/button.html', {'form': form})


class UserNew (TemplateView):
    template_name = 'home/button.html'

    def user_new(self,request):
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = UserForm()
        return render(request, 'home/button.html', {'form': form})

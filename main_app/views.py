from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from.forms import LoginForm
from .models import Skill

def home(request):
    return render(request, 'home.html')


## Todo: add error message for this view function
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# Todo add error message if credentials are wrong
def login_view(request):
    error_message = ''
    if request.method == 'POST':
        next = request.POST.get('next') or None
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and next is not None:
                login(request, user)
                return redirect(next)
            elif user is not None and next is None:
                login(request, user)
                return redirect('home')
            else:
                error_message = 'Sorry, your username or password was invalid'
    
    form = LoginForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


class CreateSkill(LoginRequiredMixin, CreateView):
    model = Skill
    fields = ['skill', 'skill_level']
    template_name = 'skills/skill_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SkillsIndex(LoginRequiredMixin, ListView):
    template_name = 'skills/skills_index.html'

    def get_queryset(self):
        return self.request.user.skill_set.all()

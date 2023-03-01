from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

User = get_user_model()

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username,
                                 password=password)
        login(request, user)
        return redirect('login')
    return render(request, 'users/signup.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'users/login.html', {'error': 'Les informations d\'identification sont incorrectes.'})
    return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    return redirect('index')


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'users/register_user.html', {'form': form})

@staff_member_required
def addToPremiumGroup(request):
    group = Group.objects.get(name='premium')
    request.user.groups.add(group)
    return HttpResponse('<h1>a ete ajouter avec succes dans le premium</h1>')
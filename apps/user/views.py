from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from .forms import LoginForm, RegisterForm, EditForm


def login(request):
    title = 'вход'
    login_form = LoginForm(data=request.POST or None)
    next = request.GET['next'] if 'next' in request.GET.keys() else ''
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('main'))
    return render(request, 'user/login.html', {'title': title, 'login_form': login_form, 'next': next})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    title = 'регистрация'
    if request.method == 'POST':
        register_form = RegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('user:login'))
    else:
        register_form = RegisterForm()

    content = {'title': title, 'register_form': register_form}

    return render(request, 'user/register.html', content)


def edit(request):
    title = 'редактирование'
    if request.method == 'POST':
        edit_form = EditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('user:edit'))
    else:
        edit_form = EditForm(instance=request.user)

    content = {'title': title, 'edit_form': edit_form}
    return render(request, 'user/edit.html', content)

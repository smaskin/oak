from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from .forms import LoginForm, RegisterForm, EditForm, ProfileForm
from apps.user.models import User
from django.db import transaction


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
            user = register_form.save()
            print('сообщение подтверждения отправлено' if send_verify_mail(user) else 'ошибка отправки сообщения')
            return HttpResponseRedirect(reverse('user:login'))
    else:
        register_form = RegisterForm()

    return render(request, 'user/register.html', {'title': title, 'register_form': register_form})


@transaction.atomic
@login_required
def edit(request):
    title = 'редактирование'
    if request.method == 'POST':
        edit_form = EditForm(request.POST, request.FILES, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if edit_form.is_valid() and profile_form.is_valid:
            edit_form.save()
            return HttpResponseRedirect(reverse('user:edit'))
    else:
        edit_form = EditForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    content = {'title': title, 'edit_form': edit_form, 'profile_form': profile_form}
    return render(request, 'user/edit.html', content)


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user)
        else:
            print(f'error activation user: {user}')
        return render(request, 'user/verification.html')
    except Exception as e:
        print(f'error activation user : {e.args}')
        return HttpResponseRedirect(reverse('main'))


def send_verify_mail(user):
    verify_link = reverse('user:verify', args=[user.email, user.activation_key])
    title = f'Подтверждение учетной записи {user.username}'
    message = f'Для подтверждения учетной записи {user.username} на портале \
    {settings.DOMAIN_NAME} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

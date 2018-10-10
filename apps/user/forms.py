from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
import random, hashlib
from .models import User, Profile


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class RegisterForm(UserCreationForm):
    password2 = None

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'avatar')
        labels = {
            'email': 'Email',
            'password1': 'Пароль',
            'username': 'Имя пользователя',
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def save(self):
        user = super(RegisterForm, self).save()
        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user


class EditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'avatar')
        labels = {
            'email': 'Email',
            'password1': 'Пароль',
            'username': 'Имя пользователя',
        }

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('aboutMe', 'gender')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

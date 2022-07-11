from django import forms
from auths.models import CustomUser


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'password'
        ]
    
    repeat_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Сюда пароль второй раз!',
            'class': 'reg'}),
        label='Повторите пароль',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Сюда пароль!',
            'class': 'reg'}),
        label='Введите пароль',
    )


    def clean(self):
        data = self.cleaned_data

        if data['password'] != data['repeat_password']:
            raise forms.ValidationError('Пароли не совпадают!')


class AuthForm(forms.Form):
    email = forms.CharField(label="Email или Имя пользователя", max_length=255)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())

class EditUserInfoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'phone_number',
            'image',
        ]
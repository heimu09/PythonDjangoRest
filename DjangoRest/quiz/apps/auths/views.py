from django.http import HttpRequest
from auths.models import CustomUser
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from auths.forms import RegisterUserForm, AuthForm, EditUserInfoForm


def registr(request):
    if request.method == 'GET':
        form = RegisterUserForm()

        return render(
            request, 
            'auths/registration.html',
            context={
                'form': form
            })
    
    form = RegisterUserForm(request.POST,  request.FILES)

    if form.is_valid():
        cd = form.cleaned_data
        cd.pop('repeat_password')
        CustomUser.objects.create_user(cd.pop('email'), cd.pop('password'), **cd)
        print(CustomUser.objects.get_staff_from_date_joined())

        return redirect(reverse())
    
    return render(
        request,
        'auths/registration.html',
        context={
            'form': form
        }
    )


def auth(request):
    if request.method == 'GET':
        form = AuthForm()

        return render(
            request, 
            'auths/auth.html',
            context={
                'form': form
            })
    
    form = AuthForm(request.POST)
    if form.is_valid():
        user = authenticate(
            request=request,
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
        )

        if user:
            login(request, user)
            return redirect(reverse())

        return render(
            request=request,
            template_name='auths/auth.html',
            context={
                'form': form,
                'error': "Не верное имя пользователя или пароль"
            }
        )

    return render(
        request=request,
        template_name='auths/auth.html',
        context={'form': form}
    )


def exit(request: HttpRequest):
    logout(request)
    return redirect(reverse(auth))


def edit_user_info(request: HttpRequest):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form  = EditUserInfoForm(instance=CustomUser.objects.get(id=request.user.id))

            return render(
                request=request,
                template_name='auths/edit.html',
                context={
                    'form': form,
                }
            )

        form = EditUserInfoForm(request.POST,  request.FILES, instance=CustomUser.objects.get(id=request.user.id))

        if form.is_valid():
            form.save()
            
            return redirect(reverse(edit_user_info))
            
        return render(
            request=request,
            template_name='auths/edit.html',
            context={
                'form': form,
            }
        )

    return redirect('/user/login/')
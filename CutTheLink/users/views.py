from django.shortcuts import render, redirect
from .forms import UserRegistraionForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegistraionForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,
                             f'Аккаунт {username} был создан, введите имя пользователя и пароль для авторизации')
            return redirect('user')
    else:
        form = UserRegistraionForm()
    return render(request, 'users/registraion.html', {'form': form, 'title': 'Регистрация пользователя'})


@login_required
def profile(request):
    if request.method == "POST":
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)

        if updateUserForm.is_valid():
            updateUserForm.save()
            messages.success(request, 'Ваш аккаунт был успешно обновлен!')
            return redirect('profile')

    else:
        updateUserForm = UserUpdateForm(instance=request.user)

    return render(request, 'users/profile.html', {'form': updateUserForm})

from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from .forms import CreateUserForm, UpdateUserForm


def show_users(request):
    users_info = User.objects.all()
    return render(request, 'DB_User.html', context={'datas': users_info})


def show_infos(request, user_id):
    user = User.objects.get(id=user_id)
    messages.success(request, message=f'You are in {user.first_name} page', extra_tags='success')
    return render(request, 'user_info.html', context={'user': user})


def delete_user(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('users')


def crate_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create(first_name=cd['first_name'], last_name=cd['last_name'], bio=cd['bio'], age=cd['age'],
                                sex=cd['sex'], create=cd['create'])
            messages.success(request,
                             f"{cd['first_name'].capitalize()} {cd['last_name'].capitalize()}'s profile created successfully",
                             extra_tags='success')
            return redirect('users')
    else:
        form = CreateUserForm()
    return render(request, 'create.html', {'form': form})


def update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f'{user.first_name} infos updated', 'success')
            return redirect('users')
    else:
        form = UpdateUserForm(instance=user)
    return render(request, 'update.html', {'form': form})

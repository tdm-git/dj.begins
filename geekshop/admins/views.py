from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from users.models import User
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm


def index(request):
    return render(request, 'admins/admin.html')

@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'users': User.objects.all(),
    }
    return render(request, 'admins/admin-users-read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):

    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'admins/admin-users-create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, id):
    user_select = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, instance=user_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)
    context = {
        'title': 'Профиль',
        'user_select': user_select,
        'form': form
    }
    return render(request, 'admins/admin-users-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, id):
    user_select = User.objects.get(id=id)
    user_select.is_active = False
    user_select.save()
    # user_select.delete()
    return HttpResponseRedirect(reverse('admins:admin_users'))

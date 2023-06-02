from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from restaurant_app.forms import UserRegistrationForm, UserLoginForm, ChangePasswordForm, MakeOrder, AddPart, \
    AddTypeCorn, AddEquipment
from restaurant_app.models import Order, Equipment, CornType, Instance


def index(request):
    if not request.user.is_authenticated:
        form = UserLoginForm(data=request.POST)
        if request.method == 'POST' and form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            form = UserLoginForm
        return render(request, 'restaurant_app/index.html', {'form': form, "title": "Добро пожаловать!"})
    else:
        procceses = Order.objects.filter(client_id=request.user)
        return render(request, 'restaurant_app/index.html', {"title": "Добро пожаловать!", "procceses": procceses})


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Вы успешно зарегистрировались")
                return redirect('index')
            else:
                messages.error(request, 'Ошибка регистраций')
        else:
            form = UserRegistrationForm()
        return render(request, 'restaurant_app/register.html', {"form": form, "title": "Регистрация"})


def login_user(request):
    form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('index')
    else:
        form = UserLoginForm
    return render(request, 'restaurant_app/login.html', {'form': form, "title": "Вход!"})


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required()
def change_password(request):
    form = ChangePasswordForm(data=request.POST, user=request.user)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('logout')

    return render(request, 'restaurant_app/change-password.html', context={"form": form, "title": "Смена пароля"})


@login_required()
def add_order(request):
    form = MakeOrder()
    if request.method == 'POST':
        form = MakeOrder(request.POST)
        if form.is_valid():
            form.instance.client_id = request.user.pk
            form.save()
            return redirect('index')
    return render(request, 'restaurant_app/add-order.html', context={"form": form, 'title': 'Добавить процесс'})


def delete_order(request, pk):
    instance = get_object_or_404(Order, pk=pk)
    instance.delete()
    return redirect('index')


def add_part(request):
    form = AddPart()
    if request.method == 'POST':
        form = AddPart(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'restaurant_app/add-part.html', context={"form": form})


def add_corn_type(request):
    form = AddTypeCorn()
    if request.method == 'POST':
        form = AddTypeCorn(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'restaurant_app/add-corn-type.html', context={"form": form})


def add_equip(request):
    form = AddEquipment()
    if request.method == 'POST':
        form = AddEquipment(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'restaurant_app/add-equip.html', context={"form": form})


def get_instances(request):
    corn_types = CornType.objects.all()
    equipments = Equipment.objects.all()
    instances = Instance.objects.all()
    return render(request, 'restaurant_app/get-instances.html', context={'instances': instances,
                                                                         "equipments": equipments,
                                                                         "corn_types": corn_types,
                                                                         'title': 'Список объектов'
                                                                         })


def delete_corn_type(request, pk):
    instance = get_object_or_404(CornType, pk=pk)
    instance.delete()
    return redirect('get-instances')


def delete_equip(request, pk):
    instance = get_object_or_404(Equipment, pk=pk)
    instance.delete()
    return redirect('get-instances')


def delete_instance(request, pk):
    instance = get_object_or_404(Instance, pk=pk)
    instance.delete()
    return redirect('get-instances')


def about(request):
    return render(request, 'restaurant_app/info.html', {'title': 'О сервисе'})

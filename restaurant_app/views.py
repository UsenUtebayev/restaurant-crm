from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

from restaurant_app.forms import UserRegistrationForm, UserLoginForm, ChangePasswordForm, MakeOrder, BookingForm
from restaurant_app.models import Order, Client, Place, Booking


def index(request):
    if not request.user.is_authenticated:
        form = UserLoginForm(data=request.POST)
        if request.method == 'POST' and form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            form = UserLoginForm
        return render(request, 'restaurant_app/index.html', {'form': form, "title": "Қош келдіңіз!"})
    try:
        role = Client.objects.get(pk=request.user.pk).role
    except Client.DoesNotExist:
        role = None

    if role is None:
        orders = Order.objects.all()
        context = {"title": "Сіздің тапсырмаларыңыз", "orders": orders, "role": role, }
        return render(request, 'restaurant_app/index.html', context=context)

    if request.user.is_authenticated:
        if role.pk == 3:
            orders = Order.objects.filter(client=request.user.pk)
        elif role.pk == 2:
            orders = Order.objects.filter(cook=request.user.pk)
        else:
            orders = Order.objects.filter(waiter=request.user.pk)
        context = {"title": "Сіздің тапсырмаларыңыз", "orders": orders}
        return render(request, 'restaurant_app/index.html', context=context)


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
        return render(request, 'restaurant_app/register.html', {"form": form, "title": "Тіркелу"})


def login_user(request):
    form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('index')
    else:
        form = UserLoginForm
    return render(request, 'restaurant_app/login.html', {'form': form, "title": "Кіру!"})


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required()
def change_password(request):
    form = ChangePasswordForm(data=request.POST, user=request.user)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('logout')

    return render(request, 'restaurant_app/change-password.html', context={"form": form, "title": "Құпия сөз өзгерту"})


@login_required()
def add_order(request):
    form = MakeOrder()
    if request.method == 'POST':
        form = MakeOrder(request.POST)
        if form.is_valid():
            form.instance.client_id = request.user.pk
            form.save()
            return redirect('index')
    return render(request, 'restaurant_app/add-order.html', context={"form": form})


def delete_order(request, pk):
    instance = get_object_or_404(Order, pk=pk)
    if instance.client_id != request.user.pk:
        raise PermissionDenied('Вы не можете удалять чужие таски')
    instance.delete()
    return redirect('index')


def add_booking(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            place = Place.objects.get(pk=form.instance.taking_place.pk)
            place.is_engaged = True
            place.save(update_fields=['is_engaged'])
            form.instance.client_id = request.user.pk
            form.save()
            return redirect('index')
    return render(request, 'restaurant_app/add-booking.html', context={"form": form})


def get_bookings(request):
    bookings = None
    try:
        role = Client.objects.get(pk=request.user.pk).role
    except Client.DoesNotExist:
        role = None

    if role.pk == 1:
        bookings = Booking.objects.all()
        return render(request, 'restaurant_app/booking-list.html', context={"bookings": bookings})
    else:
        bookings = Booking.objects.filter(client=request.user.pk)
        return render(request, 'restaurant_app/booking-list.html', context={"bookings": bookings})

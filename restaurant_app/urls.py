from django.urls import path

from restaurant_app.views import change_password, index, register, login_user, logout_user, add_order, delete_order, \
    add_booking, get_bookings, get_menu

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='registration'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('change-password', change_password, name='change-password'),
    path('make-order', add_order, name='make-order'),
    path('delete-order/<int:pk>', delete_order, name='delete-order'),
    path('add-booking', add_booking, name='add-booking'),
    path('get-bookings', get_bookings, name='get-bookings'),
    path('get-menu', get_menu, name='get-menu'),
]

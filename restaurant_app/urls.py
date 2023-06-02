from django.urls import path

from restaurant_app.views import change_password, index, register, login_user, logout_user, add_order, delete_order, \
    add_part, add_corn_type, add_equip, get_instances, delete_corn_type, delete_equip, delete_instance, about

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='registration'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('change-password', change_password, name='change-password'),
    path('make-order', add_order, name='make-order'),
    path('add-part', add_part, name='add-part'),
    path('add-corn-type', add_corn_type, name='add-corn-type'),
    path('add-equip', add_equip, name='add-equip'),
    path('delete-order/<int:pk>', delete_order, name='delete-order'),
    path('get-instances', get_instances, name='get-instances'),
    path('delete-corn-type/<int:pk>', delete_corn_type, name='delete-corn-type'),
    path('delete-equip/<int:pk>', delete_equip, name='delete-equip'),
    path('delete-instance/<int:pk>', delete_instance, name='delete-instance'),
    path('info', about, name='info')
]

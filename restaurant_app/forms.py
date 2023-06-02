from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from django.forms import Select, Textarea, NumberInput, TextInput
from django.forms.utils import ErrorList

from restaurant_app.models import Order, Instance, CornType, Equipment


class CustomErrorList(ErrorList):
    def get_context(self):
        return {
            "errors": self,
            "error_class": "alert alert-danger h6 list-unstyled",
        }


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_class = CustomErrorList

    error_messages = {
        "password_mismatch": "Пароли не совпадают"
    }
    attrs = {"class": "form-control h6"}
    username = forms.CharField(label='Ваше имя', widget=forms.TextInput(attrs=attrs))
    password1 = forms.CharField(label='Ваш пароль', widget=forms.PasswordInput(attrs=attrs))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs=attrs))
    email = forms.EmailField(label='Ваша почта', widget=forms.EmailInput(attrs=attrs))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_class = CustomErrorList

    username_label = "Ваше имя"
    passwors_label = "Ваш пароль"
    username_attrs = {"class": "form-control", "placeholder": username_label}
    password_attrs = {"class": "form-control mt-3", "placeholder": passwors_label}
    username = forms.CharField(label='', widget=forms.TextInput(attrs=username_attrs))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs=password_attrs))
    error_messages = {
        "invalid_login": (
            "Проверьте правильность ."
        ),
        "inactive": "Аккаунт был забанен",
    }


class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_class = CustomErrorList

    old_password = forms.CharField(
        label="Бұрыңғы құпия сөз",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "autocomplete": "current-password", "autofocus": True}
        ),

    )
    new_password1 = forms.CharField(
        label="Жаңа құпия сөз",
        widget=forms.PasswordInput(attrs={"class": "form-control", "autocomplete": "new-password"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label="Кайталаңыз жаңа құпия сөзді",
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control", "autocomplete": "new-password"}),
    )


class MakeOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['humidity', 'temperature', 'equipment', 'instance', 'description']
        labels = {
            "humidity": "Выберите влажность",
            "temperature": "Выберите температуру",
            'equipment': "Выберите модель аппаратуры",
            'instance': "Выберите партию",
            "description": "Комментарий к процессу",
        }
        widgets = {
            "humidity": Select(attrs={"class": "form-control"}),
            "temperature": Select(attrs={"class": "form-control"}),
            "equipment": Select(attrs={"class": "form-control"}),
            "instance": Select(attrs={"class": "form-control"}),
            "description": Textarea(attrs={"class": "form-control"}),
        }


class AddPart(forms.ModelForm):
    class Meta:
        model = Instance
        fields = ['weight', 'type']
        labels = {
            "weight": "Напишите вес в килограммах",
            "type": "Выберите тип зерна",
        }
        widgets = {
            "weight": NumberInput(attrs={"class": "form-control"}),
            "type": Select(attrs={"class": "form-control"}),
        }


class AddTypeCorn(forms.ModelForm):
    class Meta:
        model = CornType
        fields = ['type', 'grade']
        labels = {
            "type": "Напишите название типа",
            "grade": "Напишите сорт зерна в цифрах от 1 до 3",
        }
        widgets = {
            "type": TextInput(attrs={"class": "form-control"}),
            "grade": NumberInput(attrs={"class": "form-control"}),
        }


class AddEquipment(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'serial_key']
        labels = {
            "name": "Напишите название аппарата",
            "serial_key": "Напишите серийный номер аппарата",
        }
        widgets = {
            "name": TextInput(attrs={"class": "form-control"}),
            "serial_key": TextInput(attrs={"class": "form-control"}),
        }

from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django import forms
from django.forms import Select, Textarea
from django.forms.utils import ErrorList

from restaurant_app.models import Client, Order, Booking, Place


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
    username = forms.CharField(label='Есіміңіз', widget=forms.TextInput(attrs=attrs))
    password1 = forms.CharField(label='Құпия сөз', widget=forms.PasswordInput(attrs=attrs))
    password2 = forms.CharField(label='Құпия сөзің тексеріңіз', widget=forms.PasswordInput(attrs=attrs))
    email = forms.EmailField(label='Сіздің поштаңыз', widget=forms.EmailInput(attrs=attrs))

    class Meta:
        model = Client
        fields = ('username', 'role', 'email', 'password1', 'password2')
        labels = {
            "role": "Сіздің рөліңіз"
        }
        widgets = {
            "role": Select(attrs={"class": "form-control"})
        }
        help_texts = {
            'role': None
        }


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_class = CustomErrorList

    username_label = "Есіміңіз"
    passwors_label = "Құпия сөз"
    username_attrs = {"class": "form-control", "placeholder": username_label}
    password_attrs = {"class": "form-control mt-3", "placeholder": passwors_label}
    username = forms.CharField(label='', widget=forms.TextInput(attrs=username_attrs))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs=password_attrs))
    error_messages = {
        "invalid_login": (
            "Қате тердіңіз."
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
        fields = ['food', 'drink', 'description', 'waiter', 'cook']
        labels = {
            "food": "Тағам",
            "drink": "Сусын",
            "description": "Даяшы мен аспазшыға ескертуіңіз",
            "waiter": "Сіздің қызметтегі даяшыңыз",
            "cook": "Егер қаласаңыз аспазшыны сайлауға болады",
        }
        widgets = {
            "food": Select(attrs={"class": "form-control"}),
            "drink": Select(attrs={"class": "form-control"}),
            "description": Textarea(attrs={"class": "form-control"}),
            "waiter": Select(attrs={"class": "form-control"}),
            "cook": Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super(MakeOrder, self).__init__(*args, *kwargs)
        self.fields['waiter'].queryset = Client.objects.filter(role_id=1)
        self.fields['cook'].queryset = Client.objects.filter(role_id=2)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['taking_place']
        labels = {
            'taking_place': "Орын сайлаңыз"
        }
        widgets = {
            "taking_place": Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, *kwargs)
        self.fields['taking_place'].queryset = Place.objects.filter(is_engaged=False)

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label="Name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg rounded-3",
                "placeholder": "Имя"
            }
        )
    )

    last_name = forms.CharField(
        max_length=30,
        required=True,
        label="Surname",
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg rounded-3",
                "placeholder": "Фамилия"
            }
        )
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg rounded-3",
                    "placeholder": "Логин"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password1"].widget.attrs.update({
            "class": "form-control form-control-lg rounded-3",
            "placeholder": "Пароль"
        })

        self.fields["password2"].widget.attrs.update({
            "class": "form-control form-control-lg rounded-3",
            "placeholder": "Повторите пароль"
        })

        self.fields["username"].help_text = None
        self.fields["password1"].help_text = None
        self.fields["password2"].help_text = None


class StyledAuthForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "form-control form-control-lg rounded-3",
            "placeholder": "Логин"
        })

        self.fields["password"].widget.attrs.update({
            "class": "form-control form-control-lg rounded-3",
            "placeholder": "Пароль"
        })
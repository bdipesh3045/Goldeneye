# student/forms.py

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Student


class StudentCreationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = [
            "first_name",
            "username",
            "last_name",
            "email",
            "phone",
            "password1",
            "password2",
        ]


class StudentAuthenticationForm(AuthenticationForm):
    pass

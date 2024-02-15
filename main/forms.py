from django import forms
from .models import contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ["first_name", "last_name", "email", "phone", "comments"]

    # def clean_phone(self):
    #     # Validate the phone number to ensure it contains only digits
    #     phone = self.cleaned_data["phone"]
    # if not phone.isdigit():
    #     raise forms.ValidationError("Phone number should contain only digits.")
    # return phone

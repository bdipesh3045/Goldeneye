from django.contrib import admin
from .models import contact

# admin.site.register(contact)


class contactAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone", "date"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "comments",
                    "date",
                ),
            },
        ),
    )
    list_per_page = 10


admin.site.register(contact, contactAdmin)

# Register your models here.

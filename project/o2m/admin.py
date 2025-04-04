from django.contrib import admin

from project.o2m.models import (
    Person,
    BloodType,
)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "blood_type",
    ]


class PersonInline(admin.StackedInline):
    model = Person
    extra = 0
    fields = [
        "id",
        "name",
    ]
    # readonly_fields = [
    #     "id",
    #     "name",
    # ]


@admin.register(BloodType)
class BloodTypeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    inlines = [
        PersonInline,
    ]

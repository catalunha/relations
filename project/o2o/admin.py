from django.contrib import admin

from project.o2o.models import (
    Person1,
    Profile,
)


class ProfileInline(admin.StackedInline):
    model = Profile
    # fields = [
    #     "id",
    #     "name",
    # ]
    readonly_fields = [
        "id",
        "name",
    ]


@admin.register(Person1)
class Person1Admin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "profile",
    ]
    inlines = [
        ProfileInline,
    ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]

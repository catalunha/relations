from django.contrib import admin

from project.m2mb.models import (
    Sauce,
    Sandwich,
    SauceSandwich,
)


# +++ Case 3b


class SauceSandwichInline(admin.StackedInline):
    model = SauceSandwich
    extra = 0
    # fields = [
    #     "id",
    #     "name",
    # ]
    # readonly_fields = [
    #     "id",
    #     "name",
    # ]


@admin.register(Sauce)
class SauceAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    inlines = [
        SauceSandwichInline,
    ]


@admin.register(Sandwich)
class SandwichAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    inlines = [
        SauceSandwichInline,
    ]


@admin.register(SauceSandwich)
class SauceSandwichAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "sauce",
        "sandwich",
        "grilled",
    ]

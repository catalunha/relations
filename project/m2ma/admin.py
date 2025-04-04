from django.contrib import admin

from project.m2ma.models import (
    Muscle,
    Exercise,
)


# +++ Case 3a


class MuscleInline(admin.StackedInline):
    model = Muscle.exercises.through
    extra = 0


@admin.register(Muscle)
class MuscleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    inlines = [
        MuscleInline,
    ]


class ExerciseInline(admin.StackedInline):
    model = Exercise.muscles.through
    extra = 0


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    exclude = ["muscles"]
    inlines = [
        ExerciseInline,
    ]

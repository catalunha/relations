from django.db import models


class Muscle(models.Model):
    # exercises
    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return f"Muscle: {self.id} {self.name}"


class Exercise(models.Model):
    name = models.CharField(
        max_length=255,
    )
    muscles = models.ManyToManyField(
        Muscle,
        related_name="exercises",
    )

    def __str__(self):
        return f"Exercise: {self.id} {self.name}"

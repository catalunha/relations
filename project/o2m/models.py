from django.db import models


class BloodType(models.Model):
    # persons
    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return f"{self.id} {self.name}"


class Person(models.Model):
    name = models.CharField(
        max_length=255,
    )
    blood_type = models.ForeignKey(
        BloodType,
        related_name="persons",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.id} {self.name}"

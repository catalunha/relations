from django.db import models


class Person1(models.Model):
    # profile
    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return f"{self.id} {self.name}"


class Profile(models.Model):
    name = models.CharField(
        max_length=255,
    )
    person1 = models.OneToOneField(
        Person1,
        related_name="profile",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.id} {self.name}"

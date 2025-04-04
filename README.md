catalunha@pop-os:~/apps/itio.net.br/relations$ uv venv --python 3.13
Using CPython 3.13.0
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
catalunha@pop-os:~/apps/itio.net.br/relations$ source .venv/bin/activate
(relations) catalunha@pop-os:~/apps/itio.net.br/relations$ uv init
Initialized project `relations`
catalunha@pop-os:~/apps/itio.net.br/relations$ 



https://www.sankalpjonna.com/learn-django/the-right-way-to-use-a-manytomanyfield-in-django
https://stackoverflow.com/questions/77205923/simple-example-of-multiple-manytomany-model-relations-in-django


# createsuperuser
username: catalunha
password: a


# models.py
```py
from django.db import models


# +++ Case 1 - o2o


class Person1(models.Model):
    # [profile](project/test/models.py)
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


# +++ Case 2 - o2m


class BloodType(models.Model):
    # [person2s](project/test/models.py)
    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return f"{self.id} {self.name}"


class Person2(models.Model):
    name = models.CharField(
        max_length=255,
    )
    blood_type = models.ForeignKey(
        BloodType,
        related_name="person2s",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.id} {self.name}"


# +++ Case 3a - m2m


class Address1(models.Model):
    # [client1s](project/test/models.py)
    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return f"Address1: {self.id} {self.name}"


class Client1(models.Model):
    name = models.CharField(
        max_length=255,
    )
    addresses = models.ManyToManyField(
        Address1,
        related_name="client1s",
    )

    def __str__(self):
        return f"Client1: {self.id} {self.name}"


# +++ Case 3b - m2m


class Address2(models.Model):
    # [address2_client2s](project/test/models.py)
    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return f"Address2: {self.id} {self.name}"


class Client2(models.Model):
    # [client2_address2s](project/test/models.py)
    name = models.CharField(
        max_length=255,
    )
    addresses = models.ManyToManyField(
        Address2,
        related_name="client2s",
        through="Client2Address2",
    )

    def __str__(self):
        return f"Client2: {self.id} {self.name}"


class Client2Address2(models.Model):
    client2 = models.ForeignKey(
        Client2, related_name="client2_address2s", on_delete=models.CASCADE
    )
    address2 = models.ForeignKey(
        Address2, related_name="address2_client2s", on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "client2",
                    "address2",
                ],
                name="Client2Address2_unique_client2_address2",
            )
        ]

    def __str__(self):
        return f"Client2Address2: {self.id}"


# +++ Case 3c - m2m


class Client3(models.Model):
    # [address3s](project/test/models.py)
    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return f"Client3: {self.id} {self.name}"


class Address3(models.Model):
    name = models.CharField(
        max_length=255,
    )
    client3 = models.ForeignKey(
        Client3,
        related_name="address3s",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"Address3: {self.id} {self.name}"
```
# admin.py
```py
from django.contrib import admin

from project.test.models import (
    Person1,
    Profile,
    Person2,
    BloodType,
    Address1,
    Client1,
    Address2,
    Client2,
    Client2Address2,
    Client3,
    Address3,
)


#  +++ Case 1
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


#  +++ Case 1


@admin.register(Person2)
class Person2Admin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "blood_type",
    ]


class Person2Inline(admin.StackedInline):
    model = Person2
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
        Person2Inline,
    ]


# +++ Case 3a


class Address1Inline(admin.StackedInline):
    model = Address1.client1s.through
    extra = 0


@admin.register(Address1)
class Address1Admin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    inlines = [
        Address1Inline,
    ]


class Client1Inline(admin.StackedInline):
    model = Client1.addresses.through
    extra = 0
    # fields = [
    #     "id",
    #     "name",
    # ]
    # readonly_fields = [
    #     "id",
    #     "name",
    # ]


@admin.register(Client1)
class Client1Admin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    exclude = ["addresses"]
    inlines = [
        Client1Inline,
    ]


# +++ Case 3b


class Client2Address2Inline(admin.StackedInline):
    model = Client2Address2
    extra = 0
    # fields = [
    #     "id",
    #     "name",
    # ]
    readonly_fields = [
        "id",
        "name",
    ]


@admin.register(Address2)
class Address2Admin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    inlines = [
        Client2Address2Inline,
    ]


@admin.register(Client2)
class Client2Admin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    inlines = [
        Client2Address2Inline,
    ]


@admin.register(Client2Address2)
class Client2Address2Admin(admin.ModelAdmin):
    list_display = [
        "id",
        "client2",
        "address2",
        "name",
    ]


# +++ Case 3c
class Address3Inline(admin.StackedInline):
    model = Address3
    extra = 0
    fields = [
        "id",
        "name",
    ]
    # readonly_fields = [
    #     "id",
    #     "name",
    # ]


@admin.register(Client3)
class Client3Admin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    inlines = [
        Address3Inline,
    ]


@admin.register(Address3)
class Address3Admin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "client3",
    ]


```




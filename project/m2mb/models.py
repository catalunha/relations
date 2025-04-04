from django.db import models


# +++ Case 3b - m2m


class Sauce(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sandwich(models.Model):
    name = models.CharField(max_length=100)
    sauces = models.ManyToManyField(Sauce, through="SauceSandwich")

    def __str__(self):
        return self.name


class SauceSandwich(models.Model):
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    sandwich = models.ForeignKey(Sandwich, on_delete=models.CASCADE)
    grilled = models.BooleanField(default=False)

    def __str__(self):
        return "{}_{}".format(self.sandwich.__str__(), self.sauce.__str__())

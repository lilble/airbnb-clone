from django.db import models

# Create your models here.

class House(models.Model):  # models.Model 상속.

    """Model Definition of Houses""" ## model에 대한 설명을 써주는 관행

    name = models.CharField(max_length=140, unique=True)
    price_per_month = models.PositiveBigIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True, help_text="Does the house allow pets?")

    def __str__(self):
        return self.name
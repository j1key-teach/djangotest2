from django.contrib.auth.models import User
from django.db import models

from rest_framework.exceptions import ValidationError


class Test(models.Model):
    question = models.CharField(max_length=255)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1, choices=[('A', 'Option_a'), ('B', 'Option_b'), ('C', 'Option_c'),
                                                             ('D', 'Option_d')])

    def __str__(self):
        return self.question


class Bolim(models.Model):
    title = models.CharField(max_length=255)
    tests = models.ManyToManyField(Test, through='BolimTest')

    def __str__(self):
        return self.title

    def clean(self):
        # Move validation logic to save method to avoid access issues
        pass

    def save(self, *args, **kwargs):
        if self.pk is not None:  # Check if the instance is already saved
            # Validate if the instance already exists
            existing_instance = Bolim.objects.get(pk=self.pk)
            if existing_instance.tests.count() > 15:
                raise ValidationError("A Bolim cannot have more than 15 tests.")

        super().save(*args, **kwargs)

        # After saving, perform validation on the related many-to-many field
        if self.pk is not None:
            if self.tests.count() > 15:
                raise ValidationError("A Bolim cannot have more than 15 tests.")


class BolimTest(models.Model):
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['bolim', 'test'], name='unique_bolim_test'),
        ]






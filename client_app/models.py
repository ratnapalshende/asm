from django.db import models

class UserRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Assuming you want to store email
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name

from django.db import models


class UserRegister(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Password = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.Name

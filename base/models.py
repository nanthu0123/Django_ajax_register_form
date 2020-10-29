from django.db import models


class UserRegister(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Password = models.CharField(max_length=20)
    Date = models.CharField(max_length=30,default=True)

    def __str__(self) -> str:
        return self.Name

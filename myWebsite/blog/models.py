from django.db import models

# Create your models here.

class postModels (models.Model):
    Nama = models.CharField(max_length=20)
    Lahir = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=30)
    alamat = models.TextField()

    def __str__(self) -> str:
        return "{}. {}".format(self.id,self.Nama)
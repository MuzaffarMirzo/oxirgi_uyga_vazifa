from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

class Kurslar(models.Model):
    kursi = models.CharField(max_length=255)
    muallifi = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['kursi']

    def __str__(self):
        return self.kursi

class Darslar(models.Model):
    dars = models.CharField(max_length=255)
    izohi = models.TextField()
    kursi = models.ForeignKey(Kurslar, on_delete=models.CASCADE, related_name="kurs_dars")
    muallifi = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'MOV', 'AVI', 'MVB'])
    ])

    class Meta:
        unique_together = ['dars']

    def __str__(self):
        return self.dars

class Izohlar(models.Model):
    darsi = models.ForeignKey(Darslar, related_name='comments', on_delete=models.CASCADE)
    muallifi = models.ForeignKey(User, on_delete=models.CASCADE)
    izohi = models.TextField()

    def __str__(self):
        return f'Comment by {self.muallif.username} on {self.dars.name}'
class LikeText(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    dars_like = models.ForeignKey(Darslar, on_delete=models.CASCADE)
    like_or_dislike = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.like_or_dislike}------{self.author}"
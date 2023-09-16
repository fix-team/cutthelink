from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Links(models.Model):
    title = models.CharField(max_length=100)
    short = models.SlugField(max_length=100, unique=True)
    long = models.URLField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ', ссылка: ' + self.title

    # def get_absolute_url(self):
    #     return reverse('news-detail', kwargs={'pk': self.pk})

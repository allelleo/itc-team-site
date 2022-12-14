from django.db import models


# Create your models here.
class FeedBack(models.Model):
    ip = models.CharField(max_length=30, default="?")
    username = models.CharField(max_length=300)
    gmail = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk}:{self.username} {' Просмотрено' if self.viewed else ' Не просмотрено!'}"

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"
        ordering = ['viewed']
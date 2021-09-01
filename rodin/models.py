from django.db import models

# Create your models here.
class News(models.Model):
    news_title = models.CharField(max_length=100, blank=False, default='Berita Roda Indonesia')
    news_description = models.TextField()
    is_published = models.BooleanField(default=True)

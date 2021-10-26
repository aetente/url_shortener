from django.db import models
from urlshortener.utils import gen_url


class UrlModel(models.Model):
    original_url = models.URLField()
    shortened_url = models.CharField(max_length=15, unique=True, blank=True)
    hits = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.shortened_url:
            self.shortened_url = gen_url(self)
        super().save(*args, **kwargs)
        return self

from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField

def get_deleted_user():
    return User.objects.get_or_create(username="ghost")[0]

class Article(models.Model):
    headline = models.CharField(max_length=255)
    short_desc = models.CharField(max_length=255, verbose_name="Short Description")
    content = MarkdownxField()
    pub_on = models.DateTimeField(auto_now_add=True, verbose_name="Published On")
    reporter = models.ForeignKey(User, on_delete=models.SET(get_deleted_user))

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('article', kwargs={'pk': self.pk})
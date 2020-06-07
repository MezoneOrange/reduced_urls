from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from django.core.validators import URLValidator


class Link(models.Model):
    """Model with links.

    long_link - char field, the link itself. Max length - 250 symbols.

    reduced_link - char field, short form of link. Max length - 50 symbols. Each name is unique.

    author - foreign key, each item belongs to a specific user. If user would be deleted his items will delete too.
    """
    long_link = models.URLField(max_length=500,
                                verbose_name="Длинная ссылка",
                                validators=[MaxLengthValidator(250), URLValidator()],)
    reduced_link = models.CharField(max_length=100,
                                    verbose_name="Сокращенная ссылка",
                                    validators=[MaxLengthValidator(20)],
                                    unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.reduced_link

    def get_absolute_url(self):
        return reverse('links', kwargs={'username': self.author})
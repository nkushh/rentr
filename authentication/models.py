from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Super Admin'),
        (2, 'Property Owner'),
        (3, 'Tenant'),
    )
    
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=2)
    phone_number = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
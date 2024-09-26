from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

from account.usermanagers import CustomUserManager

# Create your models here.:

UZBEKISTAN, QOZOGISTON, TURKIYA = "UZBEKISTAN", "QOZOGISTON", "TURKIYA"


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class UserStatus(models.TextChoices):
        ADMIN = "Admin", _("Admin")
        SELLER = "Seller", _("Seller")
        USER = "User", _("User")

    USER_COUNTRY = (
        ('UZBEKISTAN', 'Uzbekistan'),
        ('QOZOGISTON', 'Qozogiston'),
        ('TURKIYA', 'Turkiya'),
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    photo = models.ImageField(_("photo"), upload_to='user_photos/', null=True, blank=True,
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    gender = models.CharField(_("Gender"), max_length=50, choices=[("Male", "Male"), ("Female", "Female")])
    city = models.CharField(_("City"), max_length=50, null=True, blank=True)
    country = models.CharField(_("Country"), max_length=50, choices=USER_COUNTRY, null=True, blank=True, default=None)
    status = models.CharField(_("User Status"), choices=UserStatus.choices, max_length=10, default=UserStatus.USER)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Email orqali login qilinadi
    REQUIRED_FIELDS = []  # Superuser yaratishda email va paroldan boshqa maydonlar talab qilinmaydi

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'



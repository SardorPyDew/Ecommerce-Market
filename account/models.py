from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

# Create your models here.:

UZBEKISTAN, QOZOGISTON, TURKIYA = "UZBEKISTAN", "QOZOGISTON", "TURKIYA"


class CustomUser(AbstractUser):
    class UserStatus(TextChoices):
        ADMIN = "Admin", _("Admin")
        SELLER = "Seller", _("Seller")
        USER = "User", _("User")
        
    USER_COUNTRY = (
        (UZBEKISTAN, UZBEKISTAN),
        (QOZOGISTON, QOZOGISTON),
        (TURKIYA, TURKIYA),

    )
        
    email = models.EmailField(_("email address"), unique=True)
    photo = models.ImageField(_("photo"), upload_to='user_photos/', null=True, blank=True,
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
    gender = models.CharField(_("Gender"), max_length=50, choices=[("Male", "Male"), ("Female", "Female")])
    city = models.CharField(_("City"), max_length=50, null=True, blank=True),
    country = models.CharField(_("Country"), max_length=50, choices=USER_COUNTRY, default=None),
    status = models.CharField(_("User Status"), choices=UserStatus.choices, max_length=10, default=UserStatus.USER)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)
    
    def __str__(self) -> str:
        return self.get_full_name

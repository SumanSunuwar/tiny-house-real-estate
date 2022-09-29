from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"),
        max_length=30, default="+9779860733",
    )
    about_me = models.TextField(
        verbose_name=_("About me"),
        default="Say something about yourself"
    )
    license = models.CharField(
        verbose_name=_("Real Estate license"),
        max_length=20,
        blank=True,
        null=True
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"),
        default="/profile_default.png"
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20
    )
    country = CountryField(
        verbose_name=_("Country"),
        default="NE",
        blank=False,
        null=False
    )
    city = models.CharField(
        verbose_name=_("City"),
        max_length=100,
        default="Kathmandu",
        blank=False,
        null=False
    )
    is_buyer = models.BooleanField(
        verbose_name=_("Buyer"),
        default=False,
        help_text=_("Are you looking to Buy a property?")
    )
    is_seller = models.BooleanField(
        verbose_name=_("Seller"),
        default=False,
        help_text=_("Are you looking to sell a property?")
    )
    top_agent = models.BooleanField(
        verbose_name=_("Agent"),
        default=False,
    )
    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True
    )
    num_reviews = models.IntegerField(
        verbose_name=_("Number of Reviews"),
        default=0,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f"{self.user.username}'s profile"
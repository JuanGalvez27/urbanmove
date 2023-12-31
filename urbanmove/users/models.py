from django.contrib.auth.models import AbstractUser
from django.db.models import BooleanField, CharField, EmailField, TextChoices
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from urbanmove.users.managers import UserManager


class Roles(TextChoices):
    OPERATOR = "operator"
    PASSENGER = "passenger"


class User(AbstractUser):
    """
    Default custom user model for UrbanMove.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = CharField(_("Name of User"), blank=True, max_length=255)
    last_name = CharField(_("Name of User"), blank=True, max_length=255)
    email = EmailField(_("email address"), unique=True)
    username = CharField(_("Name of User"), blank=True, max_length=255)
    role = CharField(max_length=10, choices=Roles.choices, default=Roles.PASSENGER, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})

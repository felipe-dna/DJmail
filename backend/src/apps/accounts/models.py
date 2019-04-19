import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


def get_img_path(instance, filename):
    path = "{}/{}".format(instance.id, filename)
    return path


class User(AbstractUser):
    """ Herda first_name, last_name, email, password, username """
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    profile_img = models.ImageField(upload_to=get_img_path, blank=True, null=True)

    # Settings.
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'address']

    # Methods:
    def get_full_name(self):
        """ returns the full name of the user """
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.get_full_name

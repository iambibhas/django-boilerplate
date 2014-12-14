from django.db import models
from django.conf import settings
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.db.utils import DatabaseError
from django.db.models import Q
from django.utils.functional import cached_property

from eventos.common.models import TimestampedBaseModel


class Profile(TimestampedBaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="profile"
    )

    def __str__(self):
        return self.user.get_full_name()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, **kwargs):
    if kwargs['created'] is True:
        try:
            Profile.objects.create(user_id=kwargs['instance'].id)
        except DatabaseError:
            pass

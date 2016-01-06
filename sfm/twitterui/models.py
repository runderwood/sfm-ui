from django.db import models
# from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
import ui


# Create your models here.
@python_2_unicode_compatible
class TwitterSeed(ui.models.Seed):

    twitter_extra_field = models.TextField(blank=True)

    def __str__(self):
        return '<TwitterSeed %s "%s">' % (self.id, self.token)

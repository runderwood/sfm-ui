from django.db import models
# from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
import ui


@python_2_unicode_compatible
class TwitterSearchSeed(ui.models.Seed):
    query = models.TextField(blank=False)

    def __str__(self):
        return '<TwitterSearchSeed %s "%s">' % (self.id, self.token)

    @property
    def display_name(self):
        return self.query


@python_2_unicode_compatible
class TwitterUserSeed(ui.models.Seed):
    screen_name = models.TextField(blank=False)

    def __str__(self):
        return '<TwitterUserSeed %s "%s">' % (self.id, self.token)

    @property
    def display_name(self):
        return self.screen_name


@python_2_unicode_compatible
class TwitterFilterSeed(ui.models.Seed):

    name = models.TextField(blank=False)
    track = models.TextField(blank=True)
    follow = models.TextField(blank=True)
    location = models.TextField(blank=True)

    def __str__(self):
        return '<TwitterFilterSeed %s "%s">' % (self.id, self.token)

    @property
    def display_name(self):
        return self.name

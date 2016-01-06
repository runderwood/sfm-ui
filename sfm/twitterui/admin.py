from django.contrib import admin
from twitterui import models

# Register your models here.

class TwitterSeed(admin.ModelAdmin):
    fields = ('seed_set', 'token', 'uid', 'twitter_extra_field',
              'is_active',
              'is_valid', 'stats', 'date_added')
    list_display = ['seed_set', 'token', 'uid',
                    'twitter_extra_field', 'is_active',
                    'is_valid', 'stats', 'date_added', 'date_updated']
    list_filter = ['seed_set', 'token', 'uid', 'is_active',
                   'is_valid', 'stats', 'date_added', 'date_updated']
    search_fields = ['seed_set', 'token', 'uid', 'is_active',
                     'is_valid', 'stats', 'date_added', 'date_updated']


admin.site.register(models.TwitterSeed, TwitterSeed)

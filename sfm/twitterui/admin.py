from django.contrib import admin
from twitterui import models


class TwitterSearchSeed(admin.ModelAdmin):
    fields = ('seed_set', 'query', 'is_active',
              'is_valid', 'stats', 'date_added')
    list_display = ['seed_set', 'query', 'is_active',
                    'is_valid', 'stats', 'date_added', 'date_updated']
    list_filter = ['seed_set', 'query', 'is_active',
                   'is_valid', 'stats', 'date_added', 'date_updated']
    search_fields = ['seed_set', 'query', 'is_active',
                     'is_valid', 'stats', 'date_added', 'date_updated']


class TwitterUserSeed(admin.ModelAdmin):
    fields = ('seed_set', 'screen_name', 'is_active',
              'is_valid', 'stats', 'date_added')
    list_display = ['seed_set', 'screen_name', 'is_active',
                    'is_valid', 'stats', 'date_added', 'date_updated']
    list_filter = ['seed_set', 'screen_name', 'is_active',
                   'is_valid', 'stats', 'date_added', 'date_updated']
    search_fields = ['seed_set', 'scren_name', 'is_active',
                     'is_valid', 'stats', 'date_added', 'date_updated']


class TwitterFilterSeed(admin.ModelAdmin):
    fields = ('seed_set', 'name', 'track', 'follow', 'location',
              'is_active', 'is_valid', 'stats', 'date_added')
    list_display = ['seed_set', 'name', 'is_active',
                    'is_valid', 'stats', 'date_added', 'date_updated']
    list_filter = ['seed_set', 'name', 'is_active',
                   'is_valid', 'stats', 'date_added', 'date_updated']
    search_fields = ['seed_set', 'name', 'track', 'follows', 'location',
                     'is_active',
                     'is_valid', 'stats', 'date_added', 'date_updated']


admin.site.register(models.TwitterSearchSeed, TwitterSearchSeed)
admin.site.register(models.TwitterUserSeed, TwitterUserSeed)
admin.site.register(models.TwitterFilterSeed, TwitterFilterSeed)

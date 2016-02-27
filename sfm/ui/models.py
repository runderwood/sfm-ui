from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from jsonfield import JSONField
import uuid
from django.conf import settings


def default_uuid():
    return uuid.uuid4().hex


class User(AbstractUser):

    local_id = models.CharField(max_length=255, blank=True, default='',
                                help_text='Local identifier')


class Credential(models.Model):

    user = models.ForeignKey(User, related_name='credentials')
    platform = models.CharField(max_length=255, blank=True,
                                help_text='Platform name')
    token = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(default=timezone.now)


@python_2_unicode_compatible
class Collection(models.Model):

    collection_id = models.CharField(max_length=32, unique=True, default=default_uuid)
    group = models.ForeignKey(Group, related_name='collections')
    name = models.CharField(max_length=255, blank=False,
                            verbose_name='Collection name')
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    is_visible = models.BooleanField(default=True)
    stats = models.TextField(blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Collection %s "%s">' % (self.id, self.name)


@python_2_unicode_compatible
class SeedSet(models.Model):
    SCHEDULE_CHOICES = [
        (60, 'Every hour'),
        (60 * 24, 'Every day'),
        (60 * 24 * 7, 'Every week'),
        (60 * 24 * 7 * 4, 'Every 4 weeks')
    ]

    seedset_id = models.CharField(max_length=32, unique=True, default=default_uuid)
    collection = models.ForeignKey(Collection, related_name='seed_sets')
    credential = models.ForeignKey(Credential, related_name='seed_sets')
    harvest_type = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    schedule_minutes = models.PositiveIntegerField(default=60 * 24 * 7, choices=SCHEDULE_CHOICES,
                                                   verbose_name="schedule")
    harvest_options = models.TextField(blank=True)
    max_count = models.PositiveIntegerField(default=0)
    stats = models.TextField(blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(blank=True, null=True, help_text="If blank, will start now.")
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '<SeedSet %s "%s">' % (self.id, self.name)


@python_2_unicode_compatible
class Seed(models.Model):

    seed_set = models.ForeignKey(SeedSet, related_name='seeds')
    seed_id = models.CharField(max_length=32, unique=True, default=default_uuid)
    token = models.TextField(blank=True)
    uid = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    is_valid = models.BooleanField(default=True)
    stats = models.TextField(blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Seed %s "%s">' % (self.id, self.token)


class Harvest(models.Model):
    REQUESTED = "requested"
    SUCCESS = "completed success"
    FAILURE = "completed failure"
    RUNNING = "running"
    STATUS_CHOICES = (
        (REQUESTED, REQUESTED),
        (SUCCESS, SUCCESS),
        (FAILURE, FAILURE),
        (RUNNING, RUNNING)
    )
    seed_set = models.ForeignKey(SeedSet, related_name='harvests')
    harvest_id = models.CharField(max_length=32, unique=True, default=default_uuid)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=REQUESTED)
    date_requested = models.DateTimeField(blank=True, default=timezone.now)
    date_started = models.DateTimeField(blank=True, null=True)
    date_ended = models.DateTimeField(blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)
    stats = JSONField(blank=True)
    infos = JSONField(blank=True)
    warnings = JSONField(blank=True)
    errors = JSONField(blank=True)
    token_updates = JSONField(blank=True)
    uids = JSONField(blank=True)
    warcs_count = models.PositiveIntegerField(default=0)
    warcs_bytes = models.BigIntegerField(default=0)

    def __str__(self):
        return '<Harvest %s "%s">' % (self.id, self.harvest_id)


class Warc(models.Model):

    harvest = models.ForeignKey(Harvest, related_name='warcs')
    warc_id = models.CharField(max_length=32, unique=True)
    path = models.TextField()
    sha1 = models.CharField(max_length=42)
    bytes = models.PositiveIntegerField()
    date_created = models.DateTimeField()
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)


class Export(models.Model):
    REQUESTED = "requested"
    SUCCESS = "completed success"
    FAILURE = "completed failure"
    STATUS_CHOICES = (
        (REQUESTED, REQUESTED),
        (SUCCESS, SUCCESS),
        (FAILURE, FAILURE)
    )
    FORMAT_CHOICES = (
        ("csv", "Comma separated values (CSV)"),
        ("tsv", "Tab separated values (TSV)"),
        ("html", "HTML"),
        ("xlsx", "Excel (XLSX)"),
        ("json", "JSON"),
        ("json_full", "Full JSON")
    )
    user = models.ForeignKey(User, related_name='exports')
    seed_set = models.ForeignKey(SeedSet, blank=True, null=True)
    seeds = models.ManyToManyField(Seed, blank=True)
    export_id = models.CharField(max_length=32, unique=True, default=default_uuid)
    export_type = models.CharField(max_length=255)
    export_format = models.CharField(max_length=10, choices=FORMAT_CHOICES, default="csv")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=REQUESTED)
    path = models.TextField(blank=True)
    date_requested = models.DateTimeField(blank=True, default=timezone.now)
    date_started = models.DateTimeField(blank=True, null=True)
    date_ended = models.DateTimeField(blank=True, null=True)
    dedupe = models.BooleanField(blank=False, default=False)
    item_date_start = models.DateTimeField(blank=True, null=True)
    item_date_end = models.DateTimeField(blank=True, null=True)
    harvest_date_start = models.DateTimeField(blank=True, null=True)
    harvest_date_end = models.DateTimeField(blank=True, null=True)
    infos = JSONField(blank=True)
    warnings = JSONField(blank=True)
    errors = JSONField(blank=True)

    def save(self, *args, **kwargs):
        self.path = "{}/export/{}".format(settings.SFM_DATA_DIR, self.export_id)
        super(Export, self).save(*args, **kwargs)

    def __str__(self):
        return '<Export %s "%s">' % (self.id, self.export_id)

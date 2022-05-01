from django.db import models


class DjangoCeleryBeatPeriodictask(models.Model):
	name = models.CharField(unique=True, max_length=200)
	task = models.CharField(max_length=200)
	args = models.TextField()
	kwargs = models.TextField()
	queue = models.CharField(max_length=200, blank=True, null=True)
	exchange = models.CharField(max_length=200, blank=True, null=True)
	routing_key = models.CharField(max_length=200, blank=True, null=True)
	expires = models.DateTimeField(blank=True, null=True)
	enabled = models.BooleanField()
	last_run_at = models.DateTimeField(blank=True, null=True)
	total_run_count = models.IntegerField()
	date_changed = models.DateTimeField()
	description = models.TextField()
	one_off = models.BooleanField()
	start_time = models.DateTimeField(blank=True, null=True)
	priority = models.IntegerField(blank=True, null=True)
	headers = models.TextField()
	expire_seconds = models.IntegerField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'django_celery_beat_periodictask'

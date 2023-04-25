from django.db import models


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')

    class Meta:
        abstract = True

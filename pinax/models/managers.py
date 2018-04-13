from django.db import models

from .query import LogicalDeleteQuerySet


class LogicalDeletedManager(models.Manager):
    """
    A manager that serves as the default manager for `pinax.models.LogicalDeleteModel`
    providing the filtering out of logically deleted objects. In addition, it
    provides named querysets for getting the deleted objects.
    """
    def get_queryset(self):
        if self.model:
            return LogicalDeleteQuerySet(self.model, using=self._db).filter(
                date_removed__isnull=True
            )

    def all_with_deleted(self):
        if self.model:
            if hasattr(self, 'core_filters'):
                return super(LogicalDeletedManager, self).get_queryset().filter(**self.core_filters)
            return super(LogicalDeletedManager, self).get_queryset()

    def only_deleted(self):
        if self.model:
            filters = { 'date_removed__isnull': False }
            if hasattr(self, 'core_filters'):
                filters.update(**self.core_filters)
            return super(LogicalDeletedManager, self).get_queryset().filter(filters)

    def get(self, *args, **kwargs):
        return self.all_with_deleted().get(*args, **kwargs)

    def filter(self, *args, **kwargs):
        if "pk" in kwargs:
            return self.all_with_deleted().filter(*args, **kwargs)
        return self.get_queryset().filter(*args, **kwargs)

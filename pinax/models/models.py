from django.db import models
from django.utils import timezone

from . import managers
from .utils import get_related_objects


class LogicalDeleteModel(models.Model):
    """
    This base model provides date fields and functionality to enable logical
    delete functionality in derived models.
    """
    date_removed = models.DateTimeField(null=True, blank=True)

    objects = managers.LogicalDeletedManager()

    def active(self):
        return self.date_removed is None
    active.boolean = True

    def delete(self):
        # Fetch related models
        to_delete = get_related_objects(self)

        for obj in to_delete:
            obj.delete()

        # Soft delete the object
        self.date_removed = timezone.now()
        self.save()

    class Meta:
        abstract = True

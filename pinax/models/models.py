from django.db import models
from django.utils import timezone

from . import managers
from .utils import get_related_objects


class LogicalDeleteModel(models.Model):
    """
    This base model provides date fields and functionality to enable logical
    delete functionality in derived models.
    """
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)
    date_removed = models.DateTimeField(null=True, blank=True)

    objects = managers.LogicalDeletedManager()

    def active(self):
        return self.date_removed is None
    active.boolean = True

    def delete(self, _collect_related=True):
        """Soft-delete the object.

        Args:
            _collect_related(bool): is deletion of this object requires to
                collect and delete some related objects.

        `_collect_related` used with cascade deletion. Just root object
        should collect related objects. If related objects will also start to
        collect realted objects we may fail into endless recursion
        """
        # Fetch related models
        if _collect_related:
            to_delete = get_related_objects(self)
        else:
            to_delete = []

        for obj in to_delete:
            if isinstance(obj, LogicalDeleteModel):
                obj.delete(_collect_related=False)
            else:
                obj.delete()

        # Soft delete the object
        self.date_removed = timezone.now()
        self.save()

    class Meta:
        abstract = True

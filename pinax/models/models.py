from django.db import models
from django.utils import timezone

from . import managers


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

    def delete(self):
        # Fetch related models
        related_objs = [
            relation.get_accessor_name()
            for relation in self._meta.get_all_related_objects()
        ]

        for objs_model in related_objs:

            if hasattr(self, objs_model):
                local_objs_model = getattr(self, objs_model)
                if hasattr(local_objs_model, 'all'):
                    # Retrieve all related objects
                    objs = local_objs_model.all()

                    for obj in objs:
                        # Checking if inherits from logicaldelete
                        if not issubclass(obj.__class__, LogicalDeleteModel):
                            break
                        obj.delete()
                else:
                    obj = local_objs_model

                    if not issubclass(obj.__class__, LogicalDeleteModel):
                        break
                    obj.delete()

        # Soft delete the object
        self.date_removed = timezone.now()
        self.save()

    class Meta:
        abstract = True

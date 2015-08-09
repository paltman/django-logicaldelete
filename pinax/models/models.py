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

    def delete(self):
        # Fetch related models
        to_delete = get_related_objects(self)
        # Couldn't find a better way to test if itertools.chain is empty
        something_to_delete = False

        for obj in to_delete:
            something_to_delete = True
            field_nullable = False
            for field in obj._meta.fields:
                internal_type = field.get_internal_type()
                if internal_type == "ForeignKey" or internal_type == "OneToOneField":
                    if field.rel.to == self.__class__ and field.null:
                        # Set the foreignkey to None
                        setattr(obj, field.attname, None)
                        obj.save()
                        field_nullable = True
                        # Jump to the next iteration
                        continue

            if not field_nullable:
                # Only soft delete the object if there is no foreignkey field
                # with null=True
                obj.delete()
                self.date_removed = timezone.now()

        if not something_to_delete:
            self.date_removed = timezone.now()

        self.save()

    class Meta:
        abstract = True

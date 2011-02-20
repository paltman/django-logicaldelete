from django.db import models


class LogicalDeletedManager(models.Manager):
    """
    A manager that serves as the default manager for `logicaldelete.models.Model`
    providing the filtering out of logically deleted objects.  In addition, it
    provides named querysets for getting the deleted objects.
    """
    
    def get_query_set(self):
        if self.model:
            return super(LogicalDeletedManager, self).get_query_set().filter(
                date_removed__isnull=True
            )
    
    def all_with_deleted(self):
        if self.model:
            return super(LogicalDeletedManager, self).get_query_set()
    
    def only_deleted(self):
        if self.model:
            return super(LogicalDeletedManager, self).get_query_set().filter(
                date_removed__isnull=False
            )
    
    def get(self, *args, **kwargs):
        return self.all_with_deleted().get(*args, **kwargs)
    
    def filter(self, *args, **kwargs):
        if "pk" in kwargs:
            return self.all_with_deleted().filter(*args, **kwargs)
        return self.get_query_set().filter(*args, **kwargs)

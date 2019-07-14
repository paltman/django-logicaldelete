from django.contrib import admin


class LogicalDeleteModelAdmin(admin.ModelAdmin):
    """
    A base model admin to use in providing access to to logically deleted
    objects.
    """
    list_display = ("id", "__unicode__", "active")
    list_display_filter = ("active",)

    def get_queryset(self, request):
        qs = self.model._default_manager.all_with_deleted()
        ordering = self.ordering or ()
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

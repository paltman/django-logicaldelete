try:
    from django.conf.urls import patterns
except ImportError:
    patterns = None


urlpatterns = [
]

if patterns:
    urlpatterns = patterns(
        "",
    )

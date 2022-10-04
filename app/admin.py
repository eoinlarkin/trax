from django.contrib import admin
from .models import Activity


class ActivityAdmin(admin.ModelAdmin):
    """
    Class to define Activity model in the Admin dashboard
    Referencing following django documentation:
    https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.exclude
    """

    exclude = ("gpx_file", "gpx_thumb_path", "gpx_file_uploaded")


# Reginstering the Activity model and Admin panel version:
admin.site.register(Activity, ActivityAdmin)

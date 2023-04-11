from django.urls import re_path as url
from .views import BackupView

urlpatterns = [
    url(r'^backup-database-and-media/$', BackupView.as_view(), name="backup_view"),
]

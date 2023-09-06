from django.contrib import admin
from home.models import (
    Contact,
    StartUpImage,
    StoryImage,
    WorkLog
)
# Register your models here.

class WorkLogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title',)}



admin.site.register(Contact)
admin.site.register(StartUpImage)
admin.site.register(StoryImage)
admin.site.register(WorkLog,WorkLogAdmin)


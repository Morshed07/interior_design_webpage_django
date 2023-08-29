from django.contrib import admin
from home.models import (
    Contact,
    StartUpImage,
    StoryImage,
    FeaturedImage
)
# Register your models here.
admin.site.register(Contact)
admin.site.register(StartUpImage)
admin.site.register(StoryImage)
admin.site.register(FeaturedImage)

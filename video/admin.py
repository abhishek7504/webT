from django.contrib import admin
from .models import  *

class VideoAdmin(admin.ModelAdmin):
    list_filter = ['updated','timestamp']
    list_display = ['title','updated','timestamp']
    readonly_fields = ['updated','timestamp']
    search_fields = ['title']
    class Meta:
        model = Video
admin.site.register(Video,VideoAdmin)


class VideoUploadAdmin(admin.ModelAdmin):
    class Meta:
        model = VideoUpload

admin.site.register(VideoUpload,VideoUploadAdmin)

class BannerAdmin(admin.ModelAdmin):
    class Meta:
        model = Banner

admin.site.register(Banner,BannerAdmin)
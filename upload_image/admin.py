from django.contrib import admin
from upload_image.models import Images


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


admin.site.register(Images, ImagesAdmin)

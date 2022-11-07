from django.contrib import admin
from .models import Image_data, Project_images
from django.utils.safestring import mark_safe


@admin.register(Image_data)
class image_dataAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'show_item']
    list_filter = ['show_item', 'title']

@admin.register(Project_images)
class project_image_dataAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'show_item']
    list_filter = ['show_item', 'title']
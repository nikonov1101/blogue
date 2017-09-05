from django.contrib import admin

from core import models as core_models


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published_at', 'is_published', 'is_page', 'feed')
    fields = ('title', 'summary', 'body', 'url_slug', 'published_at', 'head_image', 'is_published',
              'is_page', 'created_at', 'uuid', 'lang', 'feed')
    readonly_fields = ('created_at', 'uuid')


class PostImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(core_models.Post, PostAdmin)
admin.site.register(core_models.PostImage, PostImageAdmin)

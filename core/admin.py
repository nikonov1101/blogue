from django.utils.translation import ugettext as _
from django.contrib import admin
from django.utils.safestring import mark_safe

from core import models as core_models


class BaseAdmin(admin.ModelAdmin):
    # disable selectable actions
    actions_on_top = False
    actions_on_bottom = False


class PostAdmin(BaseAdmin):
    list_display = ('id', 'title', 'published_at', 'is_published', 'is_page', 'feed')
    readonly_fields = ('preview_url',)
    fields = (
        ('url_slug', 'preview_url'),
        ('title', 'summary', 'feed'),
        'body', 'published_at', 'head_image',
        ('is_published', 'is_page', 'comments_disabled',),
    )

    def preview_url(self, obj=None):
        if obj.pk:
            return mark_safe("<a target='_blank' href='/preview/{}'>Preview</a>".format(obj.uuid))
        else:
            return _('Save the post first!')

    preview_url.short_description = _('Post preview')


class PostImageAdmin(BaseAdmin):
    fields = ('origin', 'description',)


admin.site.register(core_models.Post, PostAdmin)
admin.site.register(core_models.PostImage, PostImageAdmin)

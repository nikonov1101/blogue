from django.contrib import admin
from django.db import models
from markdownx.widgets import AdminMarkdownxWidget

from core import models as core_models


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }


class PostImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(core_models.Post, PostAdmin)
admin.site.register(core_models.Image, PostImageAdmin)

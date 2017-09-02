from django.contrib import admin
from django.db import models
from draceditor.widgets import AdminDraceditorWidget

from core import models as core_models


class PostAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.TextField: {'widget': AdminDraceditorWidget},
    # }
    pass


class PostImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(core_models.Post, PostAdmin)
admin.site.register(core_models.Image, PostImageAdmin)

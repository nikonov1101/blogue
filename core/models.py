from django.db import models
from django.utils.translation import ugettext as _

from markdownx.models import MarkdownxField

LANG_RU = 1
LANG_EN = 2
LANG_CHOICE = (
    (LANG_RU, 'Rus'),
    (LANG_EN, 'Eng'),
)


class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Title'))
    # body = models.TextField(null=False, blank=False, verbose_name=_('Body'))
    body = MarkdownxField(null=False, blank=False, verbose_name=_('Body'))
    created_at = models.DateTimeField(null=False, blank=False, auto_now_add=True, verbose_name=_('Create date'))
    published_at = models.DateTimeField(null=False, blank=False, auto_now_add=True, verbose_name=_('Publish data'))
    url_slug = models.CharField(max_length=150, null=False, blank=False, verbose_name='URL Slug')
    lang = models.PositiveSmallIntegerField(null=False, blank=False, default=LANG_RU, choices=LANG_CHOICE,
                                            verbose_name=_('Language'))
    is_published = models.BooleanField(default=False, verbose_name=_('Is published'))
    is_page = models.BooleanField(default=False, verbose_name=_('Is single page'))
    head_image = models.ForeignKey('Image', to_field='id', db_column='head_image_id', null=True, blank=True,
                                   verbose_name=_('Head image'))

    def qa(self):
        # self.body.
        pass

    class Meta:
        db_table = 'posts'
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')


class Image(models.Model):
    origin = models.ImageField(null=False, blank=False)
    preview = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(null=False, blank=False, auto_now_add=True, verbose_name=_('Create date'))
    description = models.TextField(null=False, blank=False, verbose_name=_('Description'))

    class Meta:
        db_table = 'images'
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

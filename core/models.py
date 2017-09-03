import uuid

from django.db import models
from django.utils.translation import ugettext as _
from draceditor.models import DraceditorField

LANG_RU = 1
LANG_EN = 2
LANG_CHOICE = (
    (LANG_RU, 'Rus'),
    (LANG_EN, 'Eng'),
)


class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Заголовок'))
    summary = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Общее'))
    body = DraceditorField(null=False, blank=False, verbose_name=_('История'))
    created_at = models.DateTimeField(null=False, blank=False, verbose_name=_('Создано в'))
    published_at = models.DateTimeField(null=False, blank=False, verbose_name=_('Опубликовано в'))
    uuid = models.UUIDField(null=True, blank=True, verbose_name=_('UUID'), unique=True)
    url_slug = models.CharField(max_length=150, null=False, blank=False, verbose_name='URL', unique=True)
    lang = models.PositiveSmallIntegerField(null=False, blank=False, default=LANG_RU, choices=LANG_CHOICE,
                                            verbose_name=_('Язык'))
    is_published = models.BooleanField(default=False, verbose_name=_('Опубликовано?'))
    is_page = models.BooleanField(default=False, verbose_name=_('Отдельная страница?'))
    head_image = models.ForeignKey('Image', to_field='id', db_column='head_image_id', null=True, blank=True,
                                   verbose_name=_('Картинка к посту'))

    @property
    def get_summary(self):
        return self.summary if self.summary else ''

    def __str__(self):
        return '{} {}'.format(self.title, self.published_at)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.uuid = str(uuid.uuid4())
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        db_table = 'posts'
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')
        ordering = ('-published_at',)


class Image(models.Model):
    origin = models.ImageField(null=False, blank=False)
    preview = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(null=False, blank=False, auto_now_add=True, verbose_name=_('Create date'))
    description = models.TextField(null=False, blank=False, verbose_name=_('Description'))

    class Meta:
        db_table = 'images'
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

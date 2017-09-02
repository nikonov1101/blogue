import datetime

from django.conf import settings
from django.shortcuts import render, get_object_or_404

from core import models


def get_base_ctx(page_title, page_name, page_summary):
    return dict(
        year=datetime.date.today().year,
        page_title=page_title,
        page_name=page_name,
        page_summary=page_summary,
    )


def index(request):
    posts = models.Post.objects.order_by('-published_at').exclude(is_published=False).all()[0:settings.POSTS_PER_PAGE]
    ctx = get_base_ctx(settings.SITE_NAME, settings.SITE_NAME, settings.SITE_SUMMARY)
    ctx.update({'posts': posts})
    return render(request, 'posts/index.html', ctx)


def single_post(request, slug):
    post = get_object_or_404(models.Post, url_slug=slug)
    ctx = get_base_ctx(settings.SITE_NAME, post.title, post.summary)
    ctx.update({'post': post})
    return render(request, 'posts/single_post.html', ctx)

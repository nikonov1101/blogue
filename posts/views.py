import datetime

from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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
    posts = models.Post.objects.order_by('-published_at').exclude(is_page=True).exclude(is_published=False).all()
    ctx = get_base_ctx(settings.SITE_NAME, settings.SITE_NAME, settings.SITE_SUMMARY)

    paginator = Paginator(posts, settings.POSTS_PER_PAGE)
    page = request.GET.get('page')
    try:
        paged = paginator.page(page)
    except PageNotAnInteger:
        paged = paginator.page(1)
    except EmptyPage:
        paged = paginator.page(paginator.num_pages)

    ctx.update({
        'posts':        paged,
        'is_main_page': True,
    })
    return render(request, 'posts/index.html', ctx)


def single_post(request, slug):
    post = get_object_or_404(
        models.Post,
        url_slug=slug,
        is_published=True,
    )

    ctx = get_base_ctx(post.title, post.title, post.get_summary)
    ctx.update({'post': post})
    return render(request, 'posts/single_post.html', ctx)


def single_post_preview(request, uuid):
    post = get_object_or_404(models.Post, uuid=uuid)
    ctx = get_base_ctx(post.title, post.title, post.get_summary)
    ctx.update({'post': post, 'is_preview': True})
    return render(request, 'posts/single_post.html', ctx)

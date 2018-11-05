import datetime

from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, reverse

from core import models


def main_feed_ctx(page_title, page_name, page_summary):
    return dict(
        year=datetime.date.today().year,
        page_title=page_title,
        page_name=page_name,
        page_summary=page_summary,
        home_url=reverse('blog-index'),
        show_live_link=settings.SHOW_LIVE,
        ga_id=settings.GOOGLE_ANALYTICS_ID,
        ya_id=settings.YANDEX_METRICS_ID,
        is_main_page=True,
    )


def live_feed_ctx(*args, **kwargs):
    ctx = main_feed_ctx(*args, **kwargs)
    ctx.update({
        'is_main_page': False,
        'feed':         models.FEED_LIVE,
    })
    return ctx


def post_context(post):
    ctx = dict(
        post=post,
        is_main_page=False,
        disqus_site_id=settings.DISQUS_SITE_ID,
        disqus_site_root=settings.DISQUS_SITE_ROOT,
    )

    return ctx


def preview_context(post):
    ctx = dict(
        post=post,
        is_main_page=False,
        is_preview=True,
    )

    return ctx


def _get_paged_posts(page, feed):
    posts = models.Post.objects.order_by('-published_at').exclude(is_page=True).exclude(is_published=False).filter(
        feed=feed).all()

    paginator = Paginator(posts, settings.POSTS_PER_PAGE)

    try:
        paged = paginator.page(page)
    except PageNotAnInteger:
        paged = paginator.page(1)
    except EmptyPage:
        paged = paginator.page(paginator.num_pages)

    return paged


def index_view(request):
    ctx = main_feed_ctx(settings.SITE_NAME, settings.SITE_NAME, settings.SITE_SUMMARY)
    page = request.GET.get('page')
    paged = _get_paged_posts(page, models.FEED_TECH)

    ctx.update({
        'posts': paged,
    })
    return render(request, 'posts/index.html', ctx)


def live_view(request):
    ctx = live_feed_ctx(settings.SITE_NAME, settings.LIVE_NAME, settings.LIVE_SUMMARY)
    page = request.GET.get('page')
    paged = _get_paged_posts(page, models.FEED_LIVE)

    ctx.update({
        'posts': paged,
    })
    return render(request, 'posts/live.html', ctx)


def single_post_view(request, slug):
    post = get_object_or_404(
        models.Post,
        url_slug=slug,
        is_published=True,
    )

    feed_ctx = main_feed_ctx(post.title, post.title, post.get_summary)
    post_ctx = post_context(post)
    feed_ctx.update(post_ctx)

    return render(request, 'posts/single_post.html', feed_ctx)


def single_post_preview(request, uuid):
    post = get_object_or_404(models.Post, uuid=uuid)

    feed_ctx = main_feed_ctx(post.title, post.title, post.get_summary)
    post_ctx = preview_context(post)

    feed_ctx.update(post_ctx)
    return render(request, 'posts/single_post.html', feed_ctx)


def editor(request):
    ctx = main_feed_ctx('title', 'name', 'summary')
    return render(request, 'posts/editor.html', ctx)

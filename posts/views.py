import datetime

from django.conf import settings
from django.http import JsonResponse
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
    posts = models.Post.objects.order_by('-published_at').exclude(is_page=True).exclude(is_published=False).all()[
            0:settings.POSTS_PER_PAGE]
    ctx = get_base_ctx(settings.SITE_NAME, settings.SITE_NAME, settings.SITE_SUMMARY)
    ctx.update({
        'posts': posts,
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


def tmp_import_posts(request):
    import json

    with open('/Users/alex/Downloads/sshaman.ghost.2017-09-03.json', 'r') as f:
        data = json.loads(f.read())
        posts = data['db'][0]['data']['posts']

        for post in posts:
            p = models.Post(
                title=post['title'],
                url_slug=post['slug'],
                body=post['markdown'],
                is_published=post['status'] == 'published',
                created_at=post['created_at'],
                published_at=post['published_at'],
                is_page=post['page'] == 1,
            )
            p.save()

    return JsonResponse(data={'status': 'OK'})

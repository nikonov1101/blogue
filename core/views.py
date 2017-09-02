from django.shortcuts import render
from markdownx import utils

from core import models


def index(request):
    post = models.Post.objects.first()
    md = utils.markdownify(post.body)

    return render(request, 'index.html', {'post': post, 'md': md})

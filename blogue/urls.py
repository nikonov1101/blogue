"""blogue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from posts import views as blog

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^draceditor/', include('draceditor.urls')),

    url(r'^$', blog.index, name='blog-index'),
    url(r'^post/(?P<slug>[\w-]+)/$', blog.single_post, name='blog-page'),
    url(r'^preview/(?P<uuid>[\w-]+)/$', blog.single_post_preview, name='blog-page-preview'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns.extend([
        url(r'^__import$', blog.tmp_import_posts, name='todo-remove-me'),
    ])

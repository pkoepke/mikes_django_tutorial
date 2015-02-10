from django.conf.urls import patterns, include, url

urlpatterns = patterns("",
    url(r'^all/$', 'article.views.articles'), # Matches on 'all/'. Recall that this file only gets checked if someone typed a URL with article/ in it. So this corresponds to /article/all/
    url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'), # this says there's a URL /article/get/<article_id>/. There are some regex details left out but that's essentially the idea. <article_id> will be used later.
)

from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^blog/$', views.IndexView.as_view(), name='index'),
    url(r'^blog/article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
]

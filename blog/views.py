# coding:utf-8
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Article, Category
import markdown2
from random import randint
# 20160918完成
class IndexView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = Article.objects.filter(status='p')
        for article in article_list:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
        return article_list

    # 返回随机文章列表的第一个
    def get_context_data(self, **kwargs):
        kwargs['random'] = Article.objects.all().order_by('?')[:1][0]
        return super(IndexView, self).get_context_data(**kwargs)

# 20160919
class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/detail.html"
    context_object_name = "article"

    pk_url_kwarg = 'article_id'

    def get_object(self):
        obj = super(ArticleDetailView,self).get_object()
        obj.body = markdown2.markdown(obj.body, extras=['fenced-code-blocks'], )
        return obj

    def get_context_data(self, **kwargs):
        kwargs['random'] = Article.objects.all().order_by('?')[:1][0]
        return super(DetailView, self).get_context_data(**kwargs)

# 20160919
class CategoryView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = Article.objects.filter(category=self.kwargs['cate_id'],status='p')
        # 注意在url里我们捕获了分类的id作为关键字参数（cate_id）传递给了CategoryView，
        # 传递的参数在kwargs属性中获取。
        for article in article_list:
            article.body = markdown2.markdown(article.body, )
        return article_list

    # 给视图增加额外的数据
    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        # 增加一个category_list,用于在页面显示所有分类，按照名字排序
        return super(CategoryView, self).get_context_data(**kwargs)

# 20160919
class TagsView(ListView):
    template_name = "blog/tags.html"
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = Article.objects.filter(status='p')
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = Category.objects.all().order_by('name')
        return super(TagsView, self).get_context_data(**kwargs)

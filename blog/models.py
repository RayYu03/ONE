# coding:utf-8
from django.db import models

# Create your models here.

"""
每个模型被表示为 django.db.models.Model 类的子类。
每个模型有一些类变量，它们都表示模型里的一个数据库字段。
"""
class Article(models.Model):
    """
    所有的 model 必须继承自django.db.models
    类 Aticle 即表示 Blog 的文章，一个类被 diango 映射成数据库中对应的一个表，
    表名对应类名,类的属性（field），比如下面的 title、body 等对应着数据库表的属性列

    举个栗子:

    class Person(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)

    会自动生成SQL语句

    CREATE TABLE myapp_person (
        "id" serial NOT NULL PRIMARY KEY,
        "first_name" varchar(30) NOT NULL,
        "last_name" varchar(30) NOT NULL
    );

    """

    STATUS = (
        ('d','Draft'),
        ('p','Published'),
    )

    title = models.CharField('标题',max_length=50)
    body = models.TextField('正文')
    author = models.CharField('作者',max_length=50,default='RayYu')
    created_time = models.DateTimeField('创建时间',auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间',auto_now=True)
    status = models.CharField('文章状态',max_length=1,choices=STATUS)

    # 文章摘要,允许为空,默认为正文的前300个字符
    abstract = models.CharField('摘要',max_length=300,blank=True,null=True,
                help_text='可选,默认为正文的前300个字符')

    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('赞同数', default=0)
    topped = models.BooleanField('置顶',default=False)

    """
    文章的分类，ForeignKey即数据库中的外键。
    外键的定义是：如果数据库中某个表的列的值是另外一个表的主键。
    外键定义了一个一对多的关系，这里即一篇文章对应一个分类，而一个分类下可能有多篇文章。
    on_delete=models.SET_NULL表示删除某个分类（category）后该分类下所有的Article的外键设为null（空）
    """
    category = models.ForeignKey('Category', verbose_name='分类',
                                 null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        """
        Meta包含一系列选项，这里的 ordering 表示排序，- 号表示逆序。
        即当从数据库中取出文章时，其是按文章最后一次修改时间逆序排列的。
        """
        ordering = ['-last_modified_time']

class Category(models.Model):

    name = models.CharField('类名',max_length=20)
    created_time = models.DateTimeField('创建时间',auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间',auto_now=True)

    def __str__(self):
        return self.name

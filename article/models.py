from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from markdown import Markdown
from tinymce.models import HTMLField





class Tag(models.Model):
    text = models.CharField(max_length=30)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.text

class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='categories')  # 添加 author 字段
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class Avatar(models.Model):
    content = models.ImageField(upload_to='avatar/%Y%m%d')






class Article(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='articles')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name='articles')
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles')
    avatar = models.ForeignKey(Avatar, null=True, blank=True, on_delete=models.SET_NULL, related_name='article')
    title = models.CharField(max_length=100)
    body = HTMLField('Text')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_md(self):
        md = Markdown(extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc'])
        md_body = md.convert(self.body)
        return md_body, md.toc

from django.contrib import admin
from .models import Article, Category, Tag, Avatar
from tinymce.widgets import TinyMCE
from django.db import models

class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
    
    # 隐藏 author 字段
    # exclude = ('author',)
    
    def save_model(self, request, obj, form, change):
        # 如果没有选择 author，则设置为当前用户
        if not obj.author:  # 检查 author 是否为空
            obj.author = request.user  # 设置当前用户为作者
        super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # 设置 author 字段的初始值为当前用户
        if 'author' in form.base_fields:
            form.base_fields['author'].initial = request.user
            # 移除帮助文本的样式
            form.base_fields['author'].help_text = "如果未选择作者，将默认使用当前用户。"
        return form

# 注册模型和自定义的 admin 类
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Avatar)

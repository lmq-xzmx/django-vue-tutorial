# models.py

from django.db import models

class ChatHistory(models.Model):
    prompt = models.TextField()  # 存储用户的提问
    response = models.TextField()  # 存储AI的回答
    created_at = models.DateTimeField(auto_now_add=True)  # 自动记录创建时间

    def __str__(self):
        return f"Prompt: {self.prompt[:50]}... Response: {self.response[:50]}..."

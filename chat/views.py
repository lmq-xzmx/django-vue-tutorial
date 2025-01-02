# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from openai import OpenAI
from .models import ChatHistory
from .serializers import ChatHistorySerializer
client = OpenAI()

# 设置 OpenAI API 密钥
#openai.api_key = 'your-api-key'

class OpenAIChatAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # 从请求中获取用户输入（假设请求体是 JSON 格式）
            user_input = request.data.get('user_input', '熊猫是熊还是猫？')

            # 调用 OpenAI API
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "你是一个英语陪练，你善于引导我使用英语与你进行交流"},
                    {"role": "user", "content": user_input}
                ]
            )

            # 获取生成的消息
            message = response.choices[0].message

            # 保存到数据库
            chat_history = ChatHistory(prompt=user_input, response=message)
            chat_history.save()

            # 序列化数据
            serializer = ChatHistorySerializer(chat_history)

            # 返回 JSON 响应
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            # 处理异常并返回错误信息
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

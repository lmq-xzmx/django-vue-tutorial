from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Post
from .serializers import PostSerializer
from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['post'])
    def get_user_input(self, request):
        user_input = request.data.get('user_input')
        assistant = Assistant(tools=[DuckDuckGo()], show_tool_calls=True)
        response = assistant.run(user_input, markdown=True, stream=False)
        
        if not response:
            response = "没有收到有效反馈"

        post = Post.objects.create(question=user_input, response=response)
        serializer = self.get_serializer(post)
        return Response(serializer.data)

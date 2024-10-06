from django.shortcuts import render
#views-使用django模版
from .models import Post
from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo

def get_user_input(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        assistant = Assistant(tools=[DuckDuckGo()], show_tool_calls=True)
        response = assistant.run(user_input, markdown=True,stream=False)
        print("response:",type(response))
        #response = assistant.print_response(user_input, markdown=True)
        # 处理响应为空的情况
        if not response:
            response = "没有收到有效反馈"


        post = Post.objects.create(question=user_input, response=response)
        posts = Post.objects.all()
        return render(request, 'response_page.html', {'post': post, 'posts': posts})
    
    posts = Post.objects.all()
    return render(request, 'response_page.html', {'posts': posts})



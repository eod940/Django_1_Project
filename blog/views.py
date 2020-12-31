from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.
# 어떠한 model을 template에 담아주는 방식 사용 => FBV(function based view) -> CBV(class based view)

class PostList(ListView):
    model = Post

    def get_queryset(self):
        # 최신순으로 정렬
        return Post.objects.order_by('-created')

class PostDetail(DetailView):
    model = Post

# def post_detail(request, pk):
#     blog_post = Post.objects.get(pk=pk)

#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'blog_post':blog_post,
#         }
#     )
# def index(request):
#     posts = Post.objects.all()

    # return render(
    #     request,
    #     'blog/index.html',
    #     {
    #         'posts': posts,
    #     }
    # )
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    # reemplaze el codigo original con este
    #que automaticamente manejas las expciones en el paginado

   # posts = Post.published.all() preview code in this funtion
    
    return render(request,'blog/post/list.html',{'posts': posts})
#elimine contexto 'page':page para verificar que no se utilizaba en la pagina listado
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,status='published',
    publish__year=year,
    publish__month=month,
    publish__day=day)
    return render(request,'blog/post/detail.html',{'post': post})
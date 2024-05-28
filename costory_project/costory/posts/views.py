from django.views.generic import (
    CreateView,ListView,DetailView,UpdateView,DeleteView,RedirectView
)
from django.urls import reverse
from .models import post
from .forms import postform

# Create your views here.
# def post_list(request):
#     posts=post.objects.all()
#     paginator=Paginator(posts,6)
#     curr_page_number=request.GET.get('page')
#     if curr_page_number is None:
#         curr_page_number=1
#     page=paginator.page(curr_page_number)
#     return render(request,'posts/post_list.html',{'page':page})
#     context={"posts": posts}
#     return render(request,'posts/post_list.html',context)

class PostListView(ListView):
    model=post
    # template_name='posts/post_list.html' ->default value
    # context_object_name='posts'
    ordering=['-dt_created']
    paginate_by=6
    # page_kwarg='page'
    
# def post_detail(request,post_id):
#     posts=get_object_or_404(post,id=post_id)
#     context={"post":posts}
#     return render(request,'posts/post_detail.html',context)

class PostDetailView(DetailView):
    model=post
    # template_name='posts/post_detail.html'
    # pk_url_kwarg='post_id'
    # context_object_name='post'
    

# def post_create(request):
#     if request.method=='POST':
#         post_form=postform(request.POST)
#         if post_form.is_valid():
#             new_post=post_form.save()
#             return redirect('post_detail',post_id=new_post.id)
#     else:
#         post_form=postform()
#     return render(request, 'posts/post_form.html',{'form':post_form})
# --------------------
# class PostCreateView(View):
    
#     def get(self,request):
#         post_form=postform()
#         return render(request, 'posts/post_form.html',{'form':post_form})
    
#     def post(self, request):
#         post_form = postform(request.POST)
#         if post_form.is_valid():
#             new_post = post_form.save()
#             return redirect('post_detail', post_id=new_post.id)
#         return render(request, 'posts/post_form.html', {'form': post_form})


class PostCreateView(CreateView):
    model=post
    form_class=postform
    # template_name='posts/post_form.html'

    def get_success_url(self) :
        return reverse('post_detail', kwargs={'pk':self.object.id})


# def post_update(request,post_id):
#     posts=get_object_or_404(post,id=post_id)
    
#     if request.method=='POST':
#         post_form=postform(request.POST,instance=posts)
#         if post_form.is_valid():
#             post_form.save()
#             return redirect('post_detail',post_id=posts.id)
#     else: 
#         post_form=postform(instance=posts)
#     return render(request,'posts/post_form.html',{'form': post_form})


class PostUpdateView(UpdateView):
    model=post
    form_class=postform
    # template_name='posts/post_form.html'
    # pk_url_kwarg='pk'
    
    def get_success_url(self) :
        return reverse('post_detail', kwargs={'pk':self.object.id})

# def post_delete(request,post_id):
#     posts=get_object_or_404(post,id=post_id)
#     if request.method=='POST':  
#         posts.delete()
#         return redirect ('post_list')
#     else:
#         return render(request,'posts/post_confirm_delete.html',{'post':posts})


class PostDeleteView(DeleteView):
    model=post
    #template_name='posts/post_confirm_delete.html'
    #pk_url_kwarg='pk'
    #context_object_name='post'
    def get_success_url(self):
        return reverse('post_list')


# def index(request):
#     return redirect('post_list')

class IndexRedirectView(RedirectView):
    pattern_name='post_list'
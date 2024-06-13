from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView, redirectView
)
from django.urls import reverse
from .models import Post
from .forms import PostForm


# Create your views here.
#def index(request):
#    return redirect('post-list')
class IndexRedirectView(RedirectView):
    patter_name = 'post-list'

class PostListView(ListView):
    model = Post
    ordering = ['-dt_created']
    paginate_by = 6


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})


class PostDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('post-list')

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from allauth.account.models import EmailAddress
from allauth.account.views import PasswordChangeView

from braces.views import LoginRequiredMixin, UserPassesTestMixin

from .forms import PostCreateForm, PostUpdateForm, ProfileForm
from .functions import confirmation_required_redirect
from .models import Post, User


class IndexView(ListView):
    model = Post
    template_name = 'podomarket/index.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_queryset(self):
        return Post.objects.filter(is_sold=False).order_by('-dt_created')


class PostDetailView(DetailView):
    model = Post
    template_name = 'podomarket/post_detail.html'
    pk_url_kwarg = 'post_id'


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'podomarket/post_form.html'

    redirect_unauthenticated_users = True
    raise_exception = confirmation_required_redirect

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.id})

    def test_func(self, user):
        return EmailAddress.objects.filter(user=user, verified=True).exists()


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'podomarket/post_form.html'
    pk_url_kwarg = 'post_id'

    redirect_unauthenticated_users = False
    raise_exception = True

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.id})

    def test_func(self, user):
        post = self.get_object()
        return post.author == user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'podomarket/post_confirm_delete.html'
    pk_url_kwarg = 'post_id'
    
    redirect_unauthenticated_users = False
    raise_exception = True

    def get_success_url(self):
        return reverse('index')

    def test_func(self, user):
        post = self.get_object()
        return post.author == user


class ProfileView(DetailView):
    model = User
    template_name = 'podomarket/profile.html'
    pk_url_kwarg = 'user_id'
    context_object_name = 'profile_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_posts'] = Post.objects.filter(author__id=self.kwargs.get('user_id')).order_by('-dt_created')[:8]
        return context


class UserPostListView(ListView):
    model = Post
    template_name = 'podomarket/user_post_list.html'
    context_object_name = 'user_posts'
    paginate_by = 8

    def get_queryset(self):
        return Post.objects.filter(author__id=self.kwargs.get('user_id')).order_by('-dt_created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user'] = get_object_or_404(User, id=self.kwargs.get('user_id'))
        return context


class ProfileSetView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'podomarket/profile_set_form.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('index')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'podomarket/profile_update_form.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('profile', kwargs={'user_id': self.request.user.id})


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    def get_success_url(self):
        return reverse('profile', kwargs={'user_id': self.request.user.id})

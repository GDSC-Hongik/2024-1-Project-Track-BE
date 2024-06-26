from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import (
    View,
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

from braces.views import LoginRequiredMixin

from allauth.account.views import PasswordChangeView

from .mixins import LoginAndVerificationRequiredMixin, LoginAndOwnershipRequiredMixin
from .models import Review, User, Comment, Like
from .forms import ReviewForm, ProfileForm, CommentForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context['latest_reviews'] = Review.objects.all()[:4]
        user = self.request.user
        if user.is_authenticated:
            context['latest_following_reviews'] = Review.objects.filter(author__followers=user)[:4]
        return render(request, 'coplate/index.html', context)


class ReviewListView(ListView):
    model = Review
    context_object_name = 'reviews'
    template_name = 'coplate/review_list.html'
    paginate_by = 8
    
class FollowingReviewListView(LoginRequiredMixin, ListView):
    model = Review
    context_object_name = 'following_reviews'
    template_name = 'coplate/following_review_list.html'
    paginate_by = 8

    def get_queryset(self):
        return Review.objects.filter(author__followers=self.request.user)


class SearchView(ListView):
    model = Review
    context_object_name = 'search_results'
    template_name = 'coplate/search_results.html'
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        return Review.objects.filter(
            Q(title__icontains=query)
            | Q(restaurant_name__icontains=query)
            | Q(content__icontains=query)
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query', '')
        return context

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'coplate/review_detail.html'
    pk_url_kwarg = 'review_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['review_ctype_id'] = ContentType.objects.get(model='review').id
        context['comment_ctype_id'] = ContentType.objects.get(model='comment').id
        
        user = self.request.user
        if user.is_authenticated:
            review = self.object
            context['likes_review'] = Like.objects.filter(user=user, review=review).exists()
            context['liked_comments'] = Comment.objects.filter(review=review).filter(likes__user = user)
        return context


class ReviewCreateView(LoginAndVerificationRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'coplate/review_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('review-detail', kwargs={'review_id': self.object.id})
 
    

class ReviewUpdateView(LoginAndOwnershipRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'coplate/review_form.html'
    pk_url_kwarg = 'review_id'

    def get_success_url(self):
        return reverse('review-detail', kwargs={'review_id': self.object.id})


class ReviewDeleteView(LoginAndOwnershipRequiredMixin, DeleteView):
    model = Review
    template_name = 'coplate/review_confirm_delete.html'
    pk_url_kwarg = 'review_id'

  
    def get_success_url(self):
        return reverse('index') 

class CommentCreateView(LoginAndVerificationRequiredMixin, CreateView):
    http_method_names = ['post']

    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.review = Review.objects.get(id=self.kwargs.get('review_id'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('review-detail',kwargs={'review_id': self.kwargs.get('review_id')})

class CommentUpdateView(LoginAndOwnershipRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'coplate/comment_update_form.html'
    pk_url_kwarg = 'comment_id'

    def get_success_url(self):
        return reverse('review-detail', kwargs={'review_id': self.object.review.id})


class CommentDeleteView(LoginAndOwnershipRequiredMixin, DeleteView):
    model = Comment
    template_name = 'coplate/comment_confirm_delete.html'
    pk_url_kwarg = 'comment_id'

    def get_success_url(self):
        return reverse('review-detail', kwargs={'review_id': self.object.review.id})

class ProcessLikeView(LoginAndVerificationRequiredMixin, View):
    http_method_names=['post']

    def post(self, request, *args, **kwargs):
        like, created = Like.objects.get_or_create(
            user=self.request.user,
            content_type_id = self.kwargs.get('content_type_id'),
            object_id = self.kwargs.get('object_id'),
        )
        if not created:
            like.delete()

        return redirect(self.request.META['HTTP_REFERER'])

class ProfileView(DetailView):
    model = User
    template_name = 'coplate/profile.html'
    pk_url_kwarg = 'user_id'
    context_object_name = 'profile_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile_user_id = self.kwargs.get('user_id')
        if user.is_authenticated:
            context['is_following'] = user.following.filter(id=profile_user_id).exists()
        context['user_reviews'] = Review.objects.filter(author__id=profile_user_id)[:4]
        return context

class ProcessFollowView(LoginAndVerificationRequiredMixin, View):
    http_method_names=['post']

    def post(self, request, *args, **kwargs):
        user = self.request.user
        profile_user_id = self.kwargs.get('user_id')
        if user.following.filter(id=profile_user_id).exists():
            user.following.remove(profile_user_id)
        else:
            user.following.add(profile_user_id)
        return redirect('profile', user_id = profile_user_id)

class FollowingListView(ListView):
    model = User
    template_name = 'coplate/following_list.html'
    context_object_name = 'following'
    paginate_by = 10

    def get_queryset(self):
        profile_user = get_object_or_404(User, pk=self.kwargs.get('user_id'))
        return profile_user.following.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user_id'] = self.kwargs.get('user_id')
        return context

class FollowerListView(ListView):
    model = User
    template_name = 'coplate/follower_list.html'
    context_object_name = 'followers'
    paginate_by = 10

    def get_queryset(self):
        profile_user = get_object_or_404(User, pk=self.kwargs.get('user_id'))
        return profile_user.followers.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user_id'] = self.kwargs.get('user_id')
        return context


class UserReviewListView(ListView):
    model = Review
    template_name = 'coplate/user_review_list.html'
    context_object_name = 'user_reviews'
    paginate_by = 4

    def get_queryset(self):
        return Review.objects.filter(author__id=self.kwargs.get('user_id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user'] = get_object_or_404(User, id=self.kwargs.get('user_id'))
        return context


class ProfileSetView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'coplate/profile_set_form.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('index')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'coplate/profile_update_form.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('profile', kwargs={'user_id': self.request.user.id})


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    def get_success_url(self):
        return reverse('profile', kwargs={'user_id': self.request.user.id})
        
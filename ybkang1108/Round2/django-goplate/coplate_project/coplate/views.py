from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView,
)
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from allauth.account.models import EmailAddress
from allauth.account.views import PasswordChangeView
from coplate.models import Review
from coplate.forms import ReviewForm
from coplate.functions import confirmation_required_redirect

class IndexView(ListView):
    model = Review
    template_name = 'coplate/index.html'
    context_object_name = 'reviews'
    paginate_by = 4
    orderign = ['-dt_created'] # -를 붙임으로써 생성일 기준 내림차순 정렬


class ReviewDetailView(DetailView):
    model = Review
    template_name = 'coplate/review_detail.html'
    pk_url_kwarg = 'review_id'

class ReviewCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView): # minxin logic이 뷰보다 먼저 실행되어야하므로 제네릭 뷰보다 먼저 써야함
    # 이메일 확인 전 로그인 확인하기 위해서 순서 중요
    model = Review
    form_class = ReviewForm
    template_name = 'coplate/review_form.html'

    redirect_unauthenticated_users = True
    raise_exception = confirmation_required_redirect

    def form_valid(self, form):
        form.instance.author = self.request.user # 현재 유저에 접근
        return super().form_valid(form) # super은 상위 클래스인 CreateView를 의미
    
    def get_success_url(self):
        return reverse('review-detail', kwargs={'review_id': self.object.id})
    
    def test_func(self, user):
        return EmailAddress.objects.filter(user=user, verified=True).exists()

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'coplate/review_form.html'
    pk_url_kwarg = 'review_id'

    raise_exception = True # 접근 권한이 없을 때 접근하면 403 response

    def get_success_url(self):
        return reverse('review-detail', kwargs={'review_id': self.object.id})

    def test_func(self, user):
        review = self.get_object()
        return review.author == user

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'coplate/review_confirm_delete.html'
    pk_url_kwarg = 'review_id'

    raise_exception = True

    def get_success_url(self):
        return reverse('index')
    
    def test_func(self, user):
        review = self.get_object()
        return review.author == user

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')
from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView)
from django.urls import reverse
from .models import Page
from .forms import PageForm


# Create your views here.
def index(request):
    return render(request, 'diary/index.html')


def info(request):
    return render(request, 'diary/info.html')


class PageListView(ListView):
    model = Page
    ordering = ['-dt_created']
    paginate_by = 8


class PageCreateView(CreateView):
    model = Page
    form_class = PageForm

    def get_success_url(self):
        return reverse('page-detail', kwargs={'pk': self.object.id})


class PageDetailView(DetailView):
    model = Page


class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm

    def get_success_url(self):
        return reverse('page-detail', kwargs={'pk': self.object.id})


class PageDeleteView(DeleteView):
    model = Page

    def get_success_url(self):
        return reverse('page-list')

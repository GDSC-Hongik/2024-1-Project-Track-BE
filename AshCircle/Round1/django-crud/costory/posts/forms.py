from django import forms
from .models import Post
from .validators import validate_symbols
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'title',
                'placeholder': '제목을 입력하세요'}),
            'content': forms.Textarea(attrs={
                'placeholder': '내용을 입력하세요'})}

    def clean_title(self):
        title = self.cleaned_data['title']
        if '*' in title:
            raise ValidationError('*는 포함될 수 없습니다.')

        return title
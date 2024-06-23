from django import forms

from .models import User, Post


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'profile_pic',
            'nickname',
            'kakao_id',
            'address',
        ]


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'item_price',
            'item_condition',
            'item_details',
            'image1',
            'image2',
            'image3',
        ]
        widgets = {
            'item_condition': forms.RadioSelect,
        }


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'item_price',
            'item_condition',
            'item_details',
            'image1',
            'image2',
            'image3',
            'is_sold',
        ]
        widgets = {
            'item_condition': forms.RadioSelect,
        }
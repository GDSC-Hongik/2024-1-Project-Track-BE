from django import forms

from .models import User, Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'title',
            'restaurant_name',
            'restaurant_link',
            'rating',
            'image1',
            'image2',
            'image3',
            'content',
        ]
        widgets = {
            'rating': forms.RadioSelect,
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'nickname',
            'profile_pic',
            'intro',
        ]
        widgets = {
            'intro': forms.Textarea,
        }
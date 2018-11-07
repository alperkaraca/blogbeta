from django import forms
# from captcha.fields import ReCaptchaField
from .models import Post, Comment


class PostForm(forms.ModelForm):
    # captcha = ReCaptchaField()

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]


class CommentForm(forms.ModelForm):
    # captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = [
            'name',
            'content',
        ]
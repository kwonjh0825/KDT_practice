from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='리뷰 제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    content = forms.CharField(
        label='리뷰 내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        )
    )

    movie = forms.CharField(
        label='영화 제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    
    image = forms.ImageField(
        label='이미지 첨부', 
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False
    )
    
    class Meta:
        model = Article
        fields = ('title', 'content', 'movie', 'image',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='댓글',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    
    class Meta:
        model = Comment
        fields = ('content',)
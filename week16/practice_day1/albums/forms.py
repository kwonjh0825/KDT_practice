from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    content = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목 입력'
            }
        )
    )
    image = forms.ImageField(
        label='이미지',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False
    )
    class Meta:
        model = Album
        fields = '__all__'
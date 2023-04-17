from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
            label=False,
            widget=forms.TextInput(
            attrs = {
                'placeholder' : '아이디',
                'style' : 'width:200px;',
                'class': 'form-control'
            }
            )
        )
    password1 = forms.CharField(
            label=False,
            widget=forms.PasswordInput(
            attrs = {
                'placeholder' : '비밀번호',
                'style' : 'width:200px;',
                'class': 'form-control'
            }
            )
        )
    password2 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(
            attrs = {
                'placeholder' : '비밀번호 확인',
                'style' : 'width:200px;',
                'class': 'form-control'
            }
        )
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1', 'password2')



# class CustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = get_user_model()
#         fields = (
#             'email',
#             'first_name',
#             'last_name',
#         )

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'class': 'form-control',
            }
        ),
    )
    # class Meta(AuthenticationForm.Meta):
    #     model = get_user_model()
    #     fields = '__all__'
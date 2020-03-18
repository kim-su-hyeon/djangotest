from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# User모델은 우리가 직접 작성하는 것이 아닌 지원을 해주는 모델
from accounts.models import Profile


class LoginForm(forms.ModelForm):
    class Meta: # 그대로 값을 넘겨준다라고 생각하면 편하다
        model = User
        fields = ["username", "password"]


class SignupForm(UserCreationForm):
    username = forms.CharField(label='사용자명', widget=forms.TextInput(attrs={
        'pattern': '[a-zA-Z0-9]+',
        'title':'특수문자, 공백 입력 불가',
    }))

    nickname = forms.CharField(label='닉네임')
    forms.ImageField(label='프로필 사진', required=False)

    class Meta(UserCreationForm):
        fields = UserCreationForm.Meta.fields+('email', )

    def clean_nickname(self):
        # 이미 존재하는 닉네임인지 확인하는 곳
        nickname = self.cleaned_data.get('nickname')
        if Profile.objects.filter(nickname = nickname).exists():
            raise forms.ValidationError('이미 존재하는 닉네임')
        return nickname

    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("이미 존재하는 이메일")
        return email

    def clean_picture(self):
        picture = self.cleaned_data.get('picture')
        if not picture:
            picture = None
        return picture

    def save(self):
        user = super().save()
        Profile.objects.create(
            user = user,
            nickname=self.cleaned_data['nickname'],
            picture = self.cleaned_data['picture']
        )
        return user
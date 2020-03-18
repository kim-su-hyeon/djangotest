from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from .forms import SignupForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid(): # 값이 있는지 체크
            user = form.save() # form의 내용을 저장한다
            return redirect("accounts:login")

        else:
            form = SignupForm()
        return render(request, 'accounts/signup.html', {'form':form})
                # 회원가입을 요청하는 페이지로 다시 보낸다


def login_check(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        name = request.POST.get('username')
        pwd = request.POST.get("password")

        user = authenticate(username=name, password=pwd)
        # 데이터베이스에 있는 user의 정보를 비교하여 맞는 데이터를 전달해준다

        if user is not None: # 만약 user가 존재한다면
            login(request, user) # 로그인 기능이 바로 있는듯 ??
            return redirect("/")

        else:   # user가 존재하지 않다면
            return render(request, 'accounts/login_fail_info.html')

    else: # post로 들어오지 않는다면
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form' : form}) # 로그인 페이지로 이동시킨다

def logout(request):
    django_logout(request) # logout을 동작한다
    return redirect("/")
from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'), # 앞에서 이미 /를 줫기 떄문에 여기는 적지 않는다
    path('login/', login_check, name='login'),
    path('logout/', logout, name='logout'),
]
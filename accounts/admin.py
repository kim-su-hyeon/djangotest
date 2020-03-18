from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'user']
    # admin 화면에 보여질 내용
    list_display_links = ['nickname', 'user']
    # 보여진 내용중 link가 달릴 곳

    search_fields = ['nickname']
    # nickname을 통해서 검색이 가능한 창을 만든다


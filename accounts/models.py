from django.conf import settings # setting.py 내용을 사용하겟다
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


def user_path(instance, filename):
    # instance는 포토의 모델
    # filename은 업로드 되는 사진 이름
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr) # 랜덤으로 문자열을 생성
    extension = filename.split(".")[-1] # 뒤에 확장자 부분을 의미한다
    return 'accounts/{}/{}.{}'.format(instance.user.username, pid, extension)
    # instance에서 받아온 유저 정보의 이름, 랜덤 파일이름, 파일 확장명


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 사용자 정보를 관리하기 위해서 제공해주는 것
    # 사용자가 제거되면 그에 관련된 정보도 지워진다
    nickname = models.CharField('별명', max_length=20, unique=True)
    # 닉네임은 유니크 하게
    about = models.CharField(max_length=300, blank=True)
    # 빈공간을 인정한다

    picture = ProcessedImageField(upload_to = user_path,
                                  processors = [ResizeToFill(150, 150)],
                                  format='JPEG',
                                  options={'quality':90},
                                  blank=True) # 파일업로드 및 관리 설정 함수

    GENDER = (
        ('선택안함', '선택안함'),
        ('여성', '여성'),
        ('남성', '남성'),
    ) # 선택상자의 리스트를 생성한다

    gender = models.CharField('성별', max_length=10, choices=GENDER, default='N')
    # 선택상자를 만들어 주는 역할을 한다

    def __str__(self):
        return self.nickname
from django.db import models

class Post(models.Model) :
    title = models.CharField(max_length=30) # 문자를 담는 필드를 만든다.
    content = models.TextField() # 문자열의 길이 제한없는 TextField를 사용한다.

    head_image = models.ImageField(upload_to='blog/images/%y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # 월, 일,시,분,초를 기록할 수 있는 datetimefield를 가져온다.
    updated_at = models.DateTimeField(auto_now=True)
     #author : 추후 작성 예정

    def __str__(self) :
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'



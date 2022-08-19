from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
import os

class Category(models.Model) :
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    class Meta :
        verbose_name_plural = 'Categories'

class Tag(models.Model) :
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'

class Post(models.Model) :
    title = models.CharField(max_length=30) # 문자를 담는 필드를 만든다.
    hook_text = models.CharField(max_length=100, blank=True)
    content = MarkdownxField() # 문자열의 길이 제한없는 TextField를 사용한다.

    created_at = models.DateTimeField(auto_now_add=True) # 월, 일,시,분,초를 기록할 수 있는 datetimefield를 가져온다.
    updated_at = models.DateTimeField(auto_now=True)
    head_image = models.ImageField(upload_to='blog/images/%y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/images/%y/%m/%d/', blank=True)

    author = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)

    category = models.ForeignKey(Category, null=True, blank = True, on_delete = models.SET_NULL)

    tags = models.ManyToManyField(Tag,blank=True)

    def __str__(self) :
        return f'[{self.pk}]{self.title}:: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

    def get_content_markdown(self):
        return markdown(self.content)

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return f'https://doitdjango.com/avatar/id/143/e3445497d896a175/svg/ {self.author.email}'



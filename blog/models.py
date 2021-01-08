from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField(blank=True)

    slug = models.SlugField(unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/blog/category/{}/'.format(self.slug)

    class Meta:
        verbose_name_plural = 'Categories'

class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(unique=True, allow_unicode=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return '/blog/tag/{}/'.format(self.slug)

class Post(models.Model):
    # title: blog title
    title = models.CharField(max_length=30)
    content = models.TextField()
    
    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)
    #created : when
    created = models.DateTimeField()
    #만약 다른 유저가 글을올리고 계정을 삭제하면 글도 삭제 = True
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return '{} :: {}'.format(self.title, self.author)

    def get_absolute_url(self):
        return '/blog/{}/'.format(self.pk)


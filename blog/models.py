from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    # title: blog title
    title = models.CharField(max_length=30)
    content = models.TextField()
    
    #created : when
    created = models.DateTimeField()
    #만약 다른 유저가 글을올리고 계정을 삭제하면 글도 삭제 = True
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{} :: {}'.format(self.title, self.author)
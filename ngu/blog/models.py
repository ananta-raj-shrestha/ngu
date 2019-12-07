from django.db import models
from django.contrib.auth.models import User
from django import  forms
class posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    date = models.DateField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
          return self.title
# class Images(models.Model):
#     post = models.ForeignKey(posts,on_delete=models.CASCADE)
#     imge =models.ImageField(upload_to='image/',null=True,blank=True)
#     def __str__(self):
#         return f'{self.post} Image'
class PostEditForm(forms.ModelForm):
    class Meta:
        model = posts
        fields = (
            'title',
            'content',
            'date',
            'author',

        )

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = posts
        fields = (
            'title',
            'content',
            'date',
            'author',

        )
class Comment(models.Model):
    post = models.ForeignKey(posts,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    timedstamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{}-{}'.format(self.post.title,self.user.username)


from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField('Title', max_length = 200)
    blog_text = models.TextField('Text of article', default='Realy interesting article')
    pub_date = models.DateField('Date of bublication')


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_author = models.CharField('Autor name', max_length=50)
    comment_text = models.CharField('Comment text', max_length=180)
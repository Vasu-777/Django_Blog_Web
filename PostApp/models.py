from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
# from tinymce.models import HTMLField
from category.models import Category

choices={
    'General':'General',
    'Technology': 'Technology',
    'Education': 'Education',
    'Entertainment': 'Entertainment',
    'Politics': 'Politics',
    'Music': 'Music',
    'Acting': 'Acting',
    'Life skills': 'Life skills',

}


class Post(models.Model):
    image=models.ImageField(upload_to='posts_images',blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    is_published=models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail',kwargs={'pk':self.pk})

      


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    # tags = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["created_on"]

      
class Like(models.Model):
	user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

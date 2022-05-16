from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    category_slug = models.SlugField(max_length=100,unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural ='categories'

    def get_url(self):#Canonical Url
        return reverse('blogs_by_category',args=[self.category_slug])
    def __str__(self):
        return self.category_name
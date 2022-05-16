from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post
from django.template.defaultfilters import truncatewords


class LatestPostsFeed(Feed):
   title = "My blog"
   link = "/feed/"
   description = "New posts of blog"

   def items(self):
       return Post.objects.filter(is_published=True).order_by('-date_posted')[:5]

   def item_title(self, item):
       return item.title

   def item_description(self, item):
       return truncatewords(item.content,30)

   def item_link(self, item):
       return reverse('blog-detail', args=[item.pk])
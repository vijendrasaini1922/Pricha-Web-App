from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%y/%m/%d')
    caption = models.TextField(blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=1000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='posts_liked', blank=True)
    
    
    def __str__(self):
        return self.title
    
    
    def save(self, *arg, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*arg, **kwargs)
    
    class Meta : 
        ordering = ['-created'] 
        
        
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    posted_by = models.CharField(max_length=100)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body 
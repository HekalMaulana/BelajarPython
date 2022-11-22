from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.CharField(max_length=255)
    slug = models.SlugField(editable=False,blank=True)
    datePost = models.DateTimeField(auto_now_add=True,editable=False)

    def save (self):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self) -> str:
        return "{}. {}".format(self.id,self.title)
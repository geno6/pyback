from django.db import models
from django.conf import settings
from os import path


class Tag(models.Model):
    list_per_page = 10

    title = models.CharField(max_length=255)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    list_per_page = 10

    title = models.CharField(max_length=255)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Post(models.Model):
    list_per_page = 10

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
    body = models.TextField()
    active = models.BooleanField()
    ordering = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        model = self.__class__

        if self.ordering is None:
            try:
                last = model.objects.order_by('-ordering')[0]
                self.ordering = last.ordering + 1
            except IndexError:
                self.ordering = 0

        return super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey('Post', related_name='images')
    image = models.ImageField(upload_to=path.join(settings.PROJECT_PATH, 'static/files/blog/posts'))
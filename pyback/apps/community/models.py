from django.db import models


class Community(models.Model):
    list_per_page = 10

    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.IntegerField()
    status = models.IntegerField()
    code = models.CharField(max_length=8)
    ordering = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
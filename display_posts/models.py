from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=50, blank=False, null=False)
    post_text = models.TextField(blank=False, null=False)
    date_posted = models.DateTimeField(blank=True, null=True)
    is_reviewed = models.BooleanField(default=False, verbose_name="Reviewed?")
    
    def __str__(self):
        return self.author
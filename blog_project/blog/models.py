from django.db import models

class BlogPost(models.Model):
    title = models.CharField(verbose_name="სათაური", max_length=255)
    content = models.TextField(verbose_name="ტექსტი")
    created_at = models.DateTimeField(verbose_name="შექმნის თარიღი",auto_now_add=True)
    category = models.CharField(verbose_name="კატეგორია", max_length=255)
    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ['created_at']



    def __str__(self):
        return self.title
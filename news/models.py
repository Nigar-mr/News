from django.db import models

# Create your models here.



class HeaderModel(models.Model):
    title = models.CharField(max_length=20)

class News(models.Model):
    image = models.ImageField(upload_to="news/", null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    modal_text = models.TextField(null=True, blank=True)
    url = models.TextField(null=True,blank=True)

    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


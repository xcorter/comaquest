from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):
    text = RichTextField()


class Slider(models.Model):
    image = models.ImageField(upload_to = "images/")

    def admin_image(self):
        return '<img src="%s" height="100" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = 'Image'
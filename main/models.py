from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):
    text = RichTextField()


class Contact(models.Model):
    text = RichTextField()


class Slider(models.Model):
    image = models.ImageField(upload_to = "images/")

    def admin_image(self):
        return '<img src="%s" height="100" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = 'Image'


class Quest(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="quest_images/", verbose_name="Изображение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Квест"
        verbose_name_plural = "Квесты"


class QuestImage(models.Model):
    quest = models.ForeignKey(Quest, verbose_name="Квест")
    image = models.ImageField(upload_to = "quests_images/", verbose_name="Изображение")
    thumbnail = models.ImageField(upload_to = "preview_quests_images/", verbose_name="Превью 200 на 200")
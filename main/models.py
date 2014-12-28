from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):
    text = RichTextField(verbose_name='Описание проекта')

    class Meta:
        verbose_name = "Описание"
        verbose_name_plural = "Описание"


class Contact(models.Model):
    text = RichTextField(verbose_name='Контакты')

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"


class Slider(models.Model):
    image = models.ImageField(upload_to = "images/", verbose_name='Изображение')

    def admin_image(self):
        return '<img src="%s" height="100" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = 'Image'

    class Meta:
        verbose_name = "Изображение слайдера"
        verbose_name_plural = "Изображения слайдера"


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
    thumbnail = models.ImageField(upload_to = "preview_quests_images/", verbose_name="Превью 121 на 110")

    def admin_image(self):
        return '%s<br/><img src="%s" height="110" />' % self.thumbnail.quest, self.thumbnail.url
    admin_image.allow_tags = True
    admin_image.short_description = 'Image'

    class Meta:
        verbose_name = "Изображение квестов"
        verbose_name_plural = "Изображения квестов"


class Time(models.Model):
    time = models.CharField(max_length=50, verbose_name='Время')

    class Meta:
        verbose_name = "Время"
        verbose_name_plural = "Время"

    def __str__(self):
        return self.title


class Order(models.Model):
    quest = models.ForeignKey(Quest, verbose_name="Квест")
    time = models.ForeignKey(Time, verbose_name="Время")
    date = models.DateField(verbose_name="Дата")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="E-mail")
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    participant_amount = models.IntegerField(max_length=2, verbose_name='Телефон', default=0)
    comment = models.TextField(verbose_name='Комментарий', default="")

    def __str__(self):
        return self.quest.title + ": " + self.time.time + ", " + self.date.isoformat()

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирование"
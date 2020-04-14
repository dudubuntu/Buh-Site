from django.db import models
from django.urls import reverse
from django.utils import timezone


class Service(models.Model):
    title = models.CharField('Название услуги', max_length=100)
    description = models.CharField('Описание', max_length=200)
    poster = models.ImageField('Постер', height_field=225)
    text = models.TextField('Текст')
    url = models.SlugField('url')
    publish = models.BooleanField('Опубликовать', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service_detail', kwargs = {'slug': self.url})

    def is_published(self):
        return True if self.publish else False

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Image(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    title = models.CharField('Имя изображения', max_length=100)
    img = models.ImageField('Изображение')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class SiteWrapper(models.Model):
    name = models.CharField('Название компании', max_length=100, default='BuhPro')
    show_about = models.BooleanField('Показывать блок About', default=True)
    about = models.CharField('Описание', max_length=500, default='Лучшие бухгалтерские услуги в Санкт-Петербурге.')
    footer_text = models.CharField('Текст снизу сайта', max_length=500, default='По всем вопросам обращайтесь по телефону или другим контактам')
    footer_link = models.CharField('Ссылка снизу сайта', max_length=500, default='Контакты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Редактор сайта'


class Index(models.Model):
    title = models.CharField('Заголовок', max_length=100, default='BuhPro')
    description = models.CharField('Описание', max_length=500, default='')
    text = models.TextField('Текст', default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стартовая страница'
        verbose_name_plural = 'Стартовые страницы'


class Guarantee(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Гарантия'
        verbose_name_plural = 'Гарантии'

class Contact(models.Model):
    choices = [
        ('phone', 'Phone'),
        ('email', 'E-mail'),
        ('other', 'Other'),
        ]
    title = models.CharField('Заголовок', max_length=50)
    type = models.CharField('Тип контакта', choices=choices, max_length=50)
    text = models.CharField('Текст', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

class ServiceRequest(models.Model):
    name = models.CharField('Имя', max_length=50)
    phone = models.CharField('Телефон', max_length=50)
    email = models.EmailField('E-mail', blank=True)
    service = models.ForeignKey(Service, models.DO_NOTHING, verbose_name='Услуга')
    description = models.TextField('Описание')
    date = models.DateTimeField('Дата', default=timezone.now())
    is_processed = models.BooleanField('Обработано', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запрос услуги'
        verbose_name_plural = 'Запрос услуг'
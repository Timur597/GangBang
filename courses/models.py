from django.db import models
from django.urls import reverse
from django.utils import timezone


class Courses(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование курса')
    description = models.TextField(blank=True, verbose_name='Информация о курсе')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    price = models.CharField(max_length=70)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    category = models.ForeignKey('Category', blank=True, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        ordering = ['title']
        verbose_name = 'Наименование курса'
        verbose_name_plural = 'Курсы'

    def get_absolute_url(self):
        return reverse('courses', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Students(models.Model):
    name = models.CharField(verbose_name='Имя студента', max_length=50)
    age = models.IntegerField(blank=True, verbose_name='Возраст студента')
    phone = models.IntegerField(blank=True, verbose_name='Номер мобильного телефона')
    email = models.EmailField()
    rating = models.IntegerField(blank=True, verbose_name='Успеваемость студента')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    courses = models.ForeignKey(Courses, on_delete=models.PROTECT, verbose_name='Курсы')

    def get_absolute_url(self):
        return reverse('students', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Teachers(models.Model):
    name = models.CharField(verbose_name='Имя преподавателя', max_length=50)
    age = models.IntegerField(blank=True, verbose_name='Возраст преподавателя')
    phone = models.IntegerField(blank=True, verbose_name='Номер мобильного телефона')
    email = models.EmailField()
    experience = models.CharField(verbose_name='Опыт', max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='Курсы')

    def get_absolute_url(self):
        return reverse('teachers', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Category(models.Model):
    title = models.CharField(max_length=150,  db_index=True, verbose_name='Категория', null=True)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



from django.conf import settings    #Строки, начинающиеся с from или import, открывают доступ к коду из других файлов.
from django.db import models        #Так что вместо того, чтобы копировать и вставлять один и тот же код во все файлы,
from django.utils import timezone   #ты можешь сослаться на него при помощи from ... import ....


class Post(models.Model): #class Post(models.Model): — эта строка определяет нашу модель (объект).
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #models.ForeignKey — ссылка на другую модель.
    title = models.CharField(max_length=200) #models.CharField — так мы определяем текстовое поле с ограничением на количество символов.
    text = models.TextField() #models.TextField — так определяется поле для неограниченно длинного текста.
    created_date = models.DateTimeField(default=timezone.now) #models.DateTimeField — дата и время.
    published_date = models.DateTimeField(blank=True, null=True) #models.DateTimeField — дата и время.

    def publish(self): #   def publish(self): Это как раз метод публикации
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # после вызова метода __str__() мы получим текст (строку) с заголовком записи.
        return self.title

    #также обрати внимание, что оба метода def publish(self): и def __str__(self): внутри класса имеют дополнительный отступ.
    # Поскольку в Python важны отступы, нам необходимо использовать их для методов внутри класса — иначе методы не будут принадлежать к классу,
    # и при запуске программы может получиться что-то неожиданное.
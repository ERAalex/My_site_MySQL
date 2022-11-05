from django.db import models


class Image_data(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField('название', max_length=50)
    artimage = models.ImageField(null=True, blank=True, upload_to='static/images/foto', verbose_name='основное изображение')
    show_item = models.BooleanField('Отобразить', default=False)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Основные картинки'
        verbose_name_plural = 'Основные картинки'
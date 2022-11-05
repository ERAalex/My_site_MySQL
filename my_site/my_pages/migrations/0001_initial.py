# Generated by Django 4.0.3 on 2022-11-05 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image_data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('artimage', models.ImageField(blank=True, null=True, upload_to='static/images/foto', verbose_name='основное изображение')),
                ('show_item', models.BooleanField(default=False, verbose_name='Отобразить')),
            ],
            options={
                'verbose_name': 'Основные картинки',
                'verbose_name_plural': 'Основные картинки',
            },
        ),
    ]
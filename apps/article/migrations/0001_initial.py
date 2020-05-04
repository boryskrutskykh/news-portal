# Generated by Django 3.0.5 on 2020-05-04 16:22

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('article_slug', autoslug.fields.AutoSlugField(allow_unicode=True, always_update=True, editable=False, populate_from='title', verbose_name='Ссылка')),
                ('description', models.TextField(null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to='')),
                ('moderation', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Статьи',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=1000)),
                ('body', models.TextField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.Article')),
            ],
            options={
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]

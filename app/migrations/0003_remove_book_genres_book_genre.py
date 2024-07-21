# Generated by Django 4.2.1 on 2023-06-05 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_genre_book_genres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genres',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
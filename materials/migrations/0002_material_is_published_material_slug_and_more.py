# Generated by Django 5.1.1 on 2024-10-17 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='опубликовано'),
        ),
        migrations.AddField(
            model_name='material',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='material',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='просмотры'),
        ),
    ]

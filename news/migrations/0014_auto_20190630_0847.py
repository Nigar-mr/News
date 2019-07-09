# Generated by Django 2.2.2 on 2019-06-30 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20190628_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='full_image',
        ),
        migrations.RemoveField(
            model_name='news',
            name='full_text',
        ),
        migrations.RemoveField(
            model_name='news',
            name='full_title',
        ),
        migrations.RemoveField(
            model_name='news',
            name='url',
        ),
        migrations.CreateModel(
            name='FullNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_image', models.ImageField(blank=True, null=True, upload_to='news/')),
                ('url', models.TextField(blank=True, null=True)),
                ('full_title', models.CharField(blank=True, max_length=100, null=True)),
                ('full_text', models.TextField(blank=True, null=True)),
                ('news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News')),
            ],
        ),
    ]
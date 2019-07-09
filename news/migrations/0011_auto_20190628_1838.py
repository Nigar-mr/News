# Generated by Django 2.2.2 on 2019-06-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_fullnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='fullnews',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fullnews',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news/'),
        ),
    ]

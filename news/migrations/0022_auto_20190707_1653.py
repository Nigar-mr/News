# Generated by Django 2.2.2 on 2019-07-07 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0021_auto_20190707_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

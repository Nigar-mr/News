# Generated by Django 2.2.2 on 2019-07-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0023_auto_20190707_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

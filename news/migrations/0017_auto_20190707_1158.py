# Generated by Django 2.2.2 on 2019-07-07 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20190707_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]

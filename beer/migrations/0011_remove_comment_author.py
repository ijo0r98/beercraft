# Generated by Django 3.1.3 on 2021-08-12 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0010_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]

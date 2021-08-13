# Generated by Django 3.1.3 on 2021-08-11 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0002_beerinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('info', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='BeerInfo',
        ),
    ]

# Generated by Django 3.0.8 on 2021-09-27 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0023_auto_20210927_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommended_Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_img', models.ImageField(upload_to='month/book/img')),
                ('book_title', models.CharField(max_length=799)),
                ('book_body', models.TextField()),
            ],
            options={
                'verbose_name_plural': ' RECOMMENDED BOOKS',
            },
        ),
    ]

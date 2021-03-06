# Generated by Django 3.0.8 on 2021-10-07 11:09

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0047_sunday_bible'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category_image', models.ImageField(upload_to='Category/img/')),
            ],
            options={
                'verbose_name_plural': 'CATEGORY',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Service/img')),
                ('img_pst', models.ImageField(upload_to='Service/pastor', verbose_name='PASTOR PICTURE')),
                ('d', models.CharField(max_length=4, verbose_name='Day')),
                ('sup', models.CharField(max_length=2, verbose_name='e.g st, nd, rd, th ')),
                ('m', models.CharField(max_length=15, verbose_name='Month')),
                ('y', models.CharField(max_length=4, verbose_name='Year')),
                ('Theme', models.CharField(max_length=678)),
                ('Theme_reference', models.CharField(max_length=899)),
                ('bible', models.CharField(max_length=79)),
                ('message', ckeditor.fields.RichTextField(verbose_name='MESSAGE')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b.Category')),
            ],
        ),
        migrations.DeleteModel(
            name='Sunday',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]

# Generated by Django 3.0.8 on 2021-10-03 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0043_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='sunday',
            name='img_pst',
            field=models.ImageField(blank=True, upload_to='test', verbose_name='PASTOR PICTURE'),
        ),
    ]
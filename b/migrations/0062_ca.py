# Generated by Django 4.0 on 2022-05-15 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0061_imgcool_alter_homecarousel_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scr', models.TextField(verbose_name='SCRIPTURE')),
                ('ref', models.CharField(max_length=100, verbose_name='BIBLE REFERENCE')),
            ],
        ),
    ]

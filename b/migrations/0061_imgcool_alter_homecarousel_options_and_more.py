# Generated by Django 4.0 on 2022-05-14 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0060_alter_choirsong_options_homecarousel_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='imgCool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=78)),
                ('date', models.DateField(default='2001/01/01')),
            ],
            options={
                'verbose_name_plural': 'FOR GALLERY',
            },
        ),
        migrations.AlterModelOptions(
            name='homecarousel',
            options={'verbose_name_plural': 'CHURCH HOME CAROUSEL'},
        ),
        migrations.AlterField(
            model_name='homecarousel',
            name='img',
            field=models.ImageField(upload_to='home/carousel'),
        ),
        migrations.CreateModel(
            name='Gal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='gallery')),
                ('number', models.CharField(max_length=5)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b.imgcool')),
            ],
            options={
                'verbose_name_plural': 'GALLERY',
            },
        ),
    ]
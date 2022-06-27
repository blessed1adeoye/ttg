# Generated by Django 3.0.8 on 2021-09-27 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0019_delete_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='BOOKS_of_the_Months',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=890)),
                ('book_1', models.CharField(blank=True, max_length=700)),
                ('book_2', models.CharField(max_length=700)),
                ('book_3', models.CharField(blank=True, max_length=700)),
                ('book_4', models.CharField(blank=True, max_length=700)),
                ('book_5', models.CharField(blank=True, max_length=700)),
            ],
            options={
                'verbose_name_plural': 'BOOKS OF THE MONTH',
            },
        ),
        migrations.DeleteModel(
            name='BOOKS_of_the_Month',
        ),
    ]

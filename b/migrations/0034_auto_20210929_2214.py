# Generated by Django 3.0.8 on 2021-09-29 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0033_auto_20210929_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommended_books',
            name='month',
            field=models.CharField(max_length=17, null=True),
        ),
        migrations.AddField(
            model_name='recommended_books',
            name='year',
            field=models.CharField(max_length=17, null=True),
        ),
    ]

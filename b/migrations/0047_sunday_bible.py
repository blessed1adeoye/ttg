# Generated by Django 3.0.8 on 2021-10-04 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0046_sunday_sup'),
    ]

    operations = [
        migrations.AddField(
            model_name='sunday',
            name='bible',
            field=models.CharField(default='deut', max_length=79),
            preserve_default=False,
        ),
    ]

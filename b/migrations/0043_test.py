# Generated by Django 3.0.8 on 2021-10-03 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0042_sunday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('img', models.ImageField(upload_to='test')),
                ('url', models.CharField(blank=True, max_length=345)),
                ('unit', models.CharField(max_length=678)),
                ('description', models.CharField(max_length=899)),
                ('mgg_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]

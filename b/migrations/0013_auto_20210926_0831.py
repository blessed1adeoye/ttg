# Generated by Django 3.0.8 on 2021-09-26 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0012_children'),
    ]

    operations = [
        migrations.CreateModel(
            name='PF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pf/img')),
                ('document', models.FileField(upload_to='pf/pdf')),
            ],
            options={
                'verbose_name_plural': 'PRAYER FORCE',
            },
        ),
        migrations.AlterModelOptions(
            name='pdf',
            options={'verbose_name_plural': 'PDF'},
        ),
    ]

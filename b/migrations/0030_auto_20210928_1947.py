# Generated by Django 3.0.8 on 2021-09-28 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0029_auto_20210928_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wofbi',
            name='bcc_graduate',
            field=models.CharField(max_length=222, verbose_name='BBC Graduation Date'),
        ),
        migrations.AlterField(
            model_name='wofbi',
            name='lcc_graduate',
            field=models.CharField(max_length=222, verbose_name='LCC Graduation Date'),
        ),
        migrations.AlterField(
            model_name='wofbi',
            name='ldc_graduate',
            field=models.CharField(max_length=222, verbose_name='LDC Graduation Date'),
        ),
    ]

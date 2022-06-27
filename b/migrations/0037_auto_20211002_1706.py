# Generated by Django 3.0.8 on 2021-10-02 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0036_technical'),
    ]

    operations = [
        migrations.CreateModel(
            name='USHERING',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=125)),
                ('residence', models.CharField(max_length=678)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('born_again', models.CharField(choices=[('Yes', 'Yes'), ('NO', 'No')], max_length=3)),
                ('joined_date', models.DateField()),
                ('new_birth_date', models.DateField()),
                ('occupation', models.CharField(max_length=678)),
                ('foundation_class', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15)),
                ('job', models.CharField(choices=[('Day', 'Day'), ('Night', 'Night'), ('Shift', 'Shift'), ('Sunday', 'Sunday')], max_length=7)),
                ('status', models.CharField(choices=[('Married', 'Married'), ('Single', 'Single'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('Divorced', 'Divorced')], max_length=9)),
                ('message', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'USHERING UNIT',
            },
        ),
        migrations.AlterModelOptions(
            name='children',
            options={'verbose_name_plural': 'CHILDREN UNIT'},
        ),
        migrations.AlterModelOptions(
            name='choir',
            options={'verbose_name_plural': 'CHOIR UNIT'},
        ),
        migrations.AlterModelOptions(
            name='decoration',
            options={'verbose_name_plural': 'DECORATION UNIT'},
        ),
        migrations.AlterModelOptions(
            name='hospitality',
            options={'verbose_name_plural': 'HOSPITALITY UNIT'},
        ),
        migrations.AlterModelOptions(
            name='security',
            options={'verbose_name_plural': 'SECURITY UNIT'},
        ),
    ]

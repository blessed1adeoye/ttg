# Generated by Django 3.0.8 on 2021-12-16 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0050_auto_20211211_0625'),
    ]

    operations = [
        migrations.CreateModel(
            name='SANCTUARY',
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
                'verbose_name_plural': 'SANTUARY UNIT',
            },
        ),
    ]

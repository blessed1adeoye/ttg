# Generated by Django 3.0.8 on 2021-09-21 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buk', models.CharField(max_length=999, verbose_name='BOOK')),
            ],
        ),
        migrations.CreateModel(
            name='Bookshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.CharField(max_length=155)),
                ('mailing_address', models.CharField(max_length=999)),
                ('email', models.EmailField(max_length=254)),
                ('book', models.CharField(choices=[('', '..CHOOSE..'), ('A', 'Anointing for Exploits'), ('B', ' Born to Win'), ('C', 'Conquering Controlling Powers'), ('D', 'The Riches of Redemption '), ('E', 'Possessing Your Possession'), ('F', 'All you Need to Have Your Needs Met'), ('G', 'In Pursuit of Vision'), ('H', 'Understanding Divine Direction'), ('I', 'Understanding Vision'), ('J', 'Following God’s Plan for your life'), ('K', 'How to be led by the Spirit'), ('L', 'Breaking the Curses of Life'), ('M', 'Pillars of Destiny'), ('N', 'Commanding the Supernatural'), ('O', 'Keys to Divine Health'), ('P', 'Pillars of Destiny'), ('Q', 'Ruling Your World'), ('R', 'Satan Get Lost'), ('S', 'Signs & Wonders Today'), ('T', 'The Blood Triumph'), ('U', 'The Healing Balm'), ('V', 'The Force of Freedom')], max_length=270)),
                ('copies', models.IntegerField()),
                ('phone', models.CharField(max_length=55)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Counsel',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(help_text='YOUR FULLNAME', max_length=489)),
                ('residential', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('church', models.CharField(max_length=333)),
                ('city', models.CharField(max_length=100)),
                ('call', models.CharField(choices=[('Yes', 'Yes'), ('NO', 'No')], max_length=3, verbose_name='Will You Want a Call Back?')),
                ('counsel', models.CharField(choices=[('Welfare', 'Welfare'), ('Education', 'Education'), ('Employment', 'Employment'), ('Family', 'Family'), ('Health/Sickness', 'Health/Sickness'), ('Travel', 'Travel'), ('Other', 'Other')], max_length=15, verbose_name='This prayer is for')),
                ('message', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('y_full_name', models.CharField(help_text='YOUR FULLNAME', max_length=489)),
                ('y_email', models.EmailField(max_length=254)),
                ('next_sunday_date', models.DateTimeField()),
                ('y_friend_full_name', models.CharField(max_length=489)),
                ('y_friend_email', models.EmailField(max_length=254)),
                ('theme', models.CharField(max_length=555)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ivpg',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('sun_no', models.IntegerField(verbose_name='date')),
                ('sun_sup', models.CharField(max_length=200)),
                ('sun_alp', models.CharField(max_length=200, verbose_name='month')),
                ('sun_year', models.BigIntegerField(default=2021, verbose_name='YEAR')),
                ('sun_img', models.ImageField(upload_to='sunday//%y/%m/%d/', verbose_name="Sunday's Image")),
                ('theme', models.CharField(max_length=999)),
            ],
            options={
                'verbose_name_plural': 'IV',
            },
        ),
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=567, verbose_name='Resource Name')),
                ('date_day', models.IntegerField()),
                ('date_month', models.CharField(max_length=256)),
                ('date_year', models.BigIntegerField(default=2021, verbose_name='YEAR')),
                ('language', models.CharField(max_length=100)),
                ('size', models.IntegerField()),
                ('document', models.FileField(upload_to='pdf')),
            ],
        ),
        migrations.CreateModel(
            name='Prayer',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(help_text='YOUR FULLNAME', max_length=489)),
                ('residential', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('church', models.CharField(max_length=333)),
                ('city', models.CharField(max_length=100)),
                ('call', models.CharField(choices=[('Yes', 'Yes'), ('NO', 'No')], max_length=3, verbose_name='Will You Want a Call Back?')),
                ('pray_for', models.CharField(choices=[('Myself', 'Myself'), ('Spouse', 'Spouse'), ('Child', 'Child'), ('Friend', 'Friend'), ('Sibling', 'Siblings')], max_length=8, verbose_name='This prayer is for')),
                ('prayer', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('t_img', models.ImageField(upload_to='Test/img', verbose_name='Testifier Image')),
                ('t_month', models.CharField(max_length=50, verbose_name='Testimony Month')),
                ('t_day', models.IntegerField(verbose_name='Testimony Day')),
                ('t_year', models.BigIntegerField(verbose_name='Testimony Year')),
                ('t_name', models.CharField(max_length=999, verbose_name='Testifier Name')),
                ('t_title', models.CharField(max_length=200, verbose_name='Testimony Title')),
                ('t_body', models.TextField(verbose_name='Testimony')),
            ],
            options={
                'verbose_name_plural': 'TESTIMONY',
            },
        ),
        migrations.CreateModel(
            name='WOFBI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Wofbi/img', verbose_name='WOFBI Image')),
            ],
            options={
                'verbose_name_plural': 'WOFBI',
            },
        ),
    ]

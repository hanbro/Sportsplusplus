# Generated by Django 2.1.7 on 2019-04-06 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_back_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ph_number',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='邮箱'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=16, verbose_name='密码'),
            preserve_default=False,
        ),
    ]
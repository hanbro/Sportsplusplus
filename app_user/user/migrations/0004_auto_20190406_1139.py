# Generated by Django 2.1.7 on 2019-04-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190406_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active',
            field=models.IntegerField(default=0, verbose_name='用户激活'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='邮箱'),
        ),
    ]
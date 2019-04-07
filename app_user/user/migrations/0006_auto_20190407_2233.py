# Generated by Django 2.1.7 on 2019-04-07 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190406_1232'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email_very',
            options={'ordering': ('date',), 'verbose_name': '验证码', 'verbose_name_plural': '验证码'},
        ),
        migrations.AlterField(
            model_name='email_very',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='邮箱'),
        ),
    ]
# Generated by Django 2.1.7 on 2019-04-07 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0006_auto_20190407_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postId', models.CharField(max_length=50, verbose_name='帖子标题')),
                ('content', models.CharField(max_length=254, verbose_name='帖子内容')),
                ('sendtime', models.DateTimeField(auto_now_add=True, verbose_name='发帖时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='帖子作者')),
            ],
            options={
                'verbose_name': '帖子',
                'verbose_name_plural': '帖子',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rplContent', models.CharField(max_length=254, verbose_name='回复内容')),
                ('rpltime', models.DateTimeField(auto_now_add=True, verbose_name='回复时间')),
                ('subPostId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Post', verbose_name='所属副帖子')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='回复作者')),
            ],
            options={
                'verbose_name': '回复',
                'verbose_name_plural': '回复',
            },
        ),
        migrations.CreateModel(
            name='SubPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subPostId', models.CharField(max_length=100, verbose_name='副帖子标题')),
                ('subContent', models.CharField(max_length=254, verbose_name='副帖子内容')),
                ('subSendtime', models.DateTimeField(auto_now_add=True, verbose_name='副帖子发帖时间')),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Post', verbose_name='所属帖子')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='副贴作者')),
            ],
            options={
                'verbose_name': '副帖子',
                'verbose_name_plural': '副帖子',
            },
        ),
    ]

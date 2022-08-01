# Generated by Django 2.2.28 on 2022-07-06 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '日志查看',
                'verbose_name_plural': '日志查看',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='默认名称', max_length=32, unique=True, verbose_name='通知方式名称')),
                ('type', models.IntegerField(choices=[(0, 'Bark'), (1, '自定义通知'), (2, '邮箱'), (3, '微信'), (4, 'Telegram')], default='邮箱', verbose_name='通知方式类型')),
                ('content', models.CharField(max_length=512, verbose_name='Key / 自定义Url')),
            ],
            options={
                'verbose_name': '通知方式',
                'verbose_name_plural': '通知方式',
            },
        ),
        migrations.CreateModel(
            name='SystemMailSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_server', models.CharField(default='localhost', max_length=32, verbose_name='邮箱服务器')),
                ('mail_port', models.IntegerField(default=25, verbose_name='端口')),
                ('mail_username', models.CharField(default='默认用户名', max_length=64, verbose_name='用户名')),
                ('mail_sender', models.CharField(default='默认用户名@mail.com', max_length=64, verbose_name='发件人')),
                ('mail_password', models.CharField(default='默认密码', max_length=64, verbose_name='密码')),
            ],
            options={
                'verbose_name': '系统邮箱',
                'verbose_name_plural': '系统邮箱',
            },
        ),
        migrations.CreateModel(
            name='TelegramSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100, verbose_name='Telegram Bot Token')),
            ],
            options={
                'verbose_name': 'Telegram Bot 设置',
                'verbose_name_plural': 'Telegram Bot 设置',
            },
        ),
    ]

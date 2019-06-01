# Generated by Django 2.2.1 on 2019-06-01 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Subject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='推文编号')),
                ('content', models.CharField(max_length=240, verbose_name='内容')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Subject.Movie', verbose_name='推荐电影')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Subject.Person', verbose_name='推荐影人')),
            ],
            options={
                'verbose_name': '动态',
                'verbose_name_plural': '动态',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(editable=False, max_length=18, primary_key=True, serialize=False, unique=True, verbose_name='用户名')),
                ('nickname', models.CharField(max_length=32, verbose_name='用户昵称')),
                ('is_active', models.BooleanField(default=True, verbose_name='用户可用')),
                ('is_admin', models.BooleanField(default=False, verbose_name='管理员用户')),
                ('feeds', models.ManyToManyField(related_name='feeds', to='User.Article', verbose_name='feeds')),
                ('following', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='我关注的人')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='历史记录编号')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='User.Article', verbose_name='文章')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='发表用户'),
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='收藏夹编号')),
                ('name', models.CharField(max_length=240, verbose_name='收藏夹名称')),
                ('private', models.BooleanField(verbose_name='是否为私有')),
                ('articles', models.ManyToManyField(to='User.Article', verbose_name='收藏的文章')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='主人')),
            ],
            options={
                'unique_together': {('user', 'name')},
            },
        ),
    ]

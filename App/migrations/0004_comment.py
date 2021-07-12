# Generated by Django 3.1.3 on 2020-12-20 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_companynotice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=128, verbose_name='内容')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('leavingmessage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.leavingmessage', verbose_name='留言')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.user', verbose_name='用户')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]

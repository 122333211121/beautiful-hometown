# Generated by Django 3.1.3 on 2020-11-23 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=10)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.department')),
            ],
            options={
                'db_table': 'position',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(default='', max_length=50)),
                ('department', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='App.department')),
                ('position', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='App.position')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='LeavingMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.user')),
            ],
            options={
                'db_table': 'leavingmessage',
            },
        ),
    ]

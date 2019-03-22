# Generated by Django 2.1.7 on 2019-03-22 08:55

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=10)),
                ('start_time', models.DateTimeField(default=datetime.datetime(2019, 3, 22, 8, 55, 31, 779161, tzinfo=utc))),
                ('end_time', models.DateTimeField(default=datetime.datetime(2019, 3, 22, 8, 55, 31, 779161, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=16)),
                ('grade', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('image', models.FilePathField()),
                ('wechat', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_vaild', models.BooleanField()),
                ('phone_number', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=16)),
                ('gender', models.CharField(max_length=2)),
                ('wechat', models.CharField(max_length=32)),
                ('hometown', models.CharField(max_length=16)),
                ('school', models.CharField(max_length=32)),
                ('majority', models.CharField(max_length=8)),
                ('identify', models.CharField(max_length=4)),
                ('address', models.CharField(max_length=32)),
                ('image', models.FilePathField()),
                ('title', models.CharField(max_length=100)),
                ('areas', models.ManyToManyField(to='information_service.Area')),
                ('subjects', models.ManyToManyField(to='information_service.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='history',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='information_service.Student'),
        ),
        migrations.AddField(
            model_name='history',
            name='volunteer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='information_service.Volunteer'),
        ),
        migrations.AddField(
            model_name='comment',
            name='volunteer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='information_service.Volunteer'),
        ),
    ]

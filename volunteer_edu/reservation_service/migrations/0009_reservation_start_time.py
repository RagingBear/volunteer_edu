# Generated by Django 2.1.3 on 2019-04-05 13:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_service', '0008_comment_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='start_time',
            field=models.CharField(default=django.utils.timezone.now, max_length=32, verbose_name='开始辅导时间'),
        ),
    ]
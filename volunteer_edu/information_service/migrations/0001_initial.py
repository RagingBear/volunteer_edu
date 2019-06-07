# Generated by Django 2.1.3 on 2019-04-06 18:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8, unique=True, verbose_name='地区名')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12, verbose_name='手机号')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('grade', models.CharField(max_length=10, verbose_name='年级')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
                ('image', models.CharField(default='http://47.105.150.105:8000/media/images/Student/student.jpg', max_length=100, verbose_name='头像')),
                ('wechat', models.CharField(max_length=32, verbose_name='微信')),
            ],
        ),
        migrations.CreateModel(
            name='StudentFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100, verbose_name='意见内容')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information_service.Student', verbose_name='学生')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True, verbose_name='学科名')),
                ('grade', models.CharField(blank=True, max_length=8, verbose_name='年级')),
                ('type', models.CharField(blank=True, max_length=8, verbose_name='学科类型')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_vaild', models.BooleanField(verbose_name='验证是否通过')),
                ('phone_number', models.CharField(max_length=12, verbose_name='手机号')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('gender', models.CharField(max_length=2, verbose_name='性别')),
                ('wechat', models.CharField(max_length=32, verbose_name='微信号')),
                ('hometown', models.CharField(max_length=16, verbose_name='籍贯')),
                ('school', models.CharField(max_length=32, verbose_name='学校')),
                ('majority', models.CharField(max_length=16, verbose_name='专业')),
                ('identify', models.CharField(max_length=4, verbose_name='目前身份')),
                ('address', models.CharField(max_length=32, verbose_name='地址')),
                ('image', models.CharField(default='http://47.105.150.105:8000/media/images/Volunteer/volunteer.png', max_length=100, verbose_name='头像')),
                ('certification', models.CharField(default='http://47.105.150.105:8000/media/images/Student/student.jpg', max_length=100, verbose_name='学生证照片')),
                ('title', models.CharField(max_length=100, verbose_name='荣誉称号')),
                ('description', models.CharField(default='', max_length=100, verbose_name='自我描述')),
                ('star_number', models.IntegerField(default=0, verbose_name='获赞数')),
                ('areas', models.ManyToManyField(to='information_service.Area', verbose_name='可教授区域')),
                ('subjects', models.ManyToManyField(to='information_service.Subject', verbose_name='教授科目')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100, verbose_name='意见内容')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information_service.Volunteer', verbose_name='志愿者')),
            ],
        ),
    ]

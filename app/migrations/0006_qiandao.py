# Generated by Django 2.2.6 on 2020-05-27 08:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_student_student_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='QianDao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qiandao', models.CharField(max_length=20, verbose_name='签到情况')),
                ('qiandao_time', models.TimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='签到时间')),
                ('Student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student')),
            ],
            options={
                'verbose_name': '姓名',
                'verbose_name_plural': '姓名',
            },
        ),
    ]

# Generated by Django 2.2.6 on 2020-05-27 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200527_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Student_password',
            field=models.CharField(max_length=200, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Student_sex',
            field=models.CharField(max_length=200, verbose_name='性别'),
        ),
    ]
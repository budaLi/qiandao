# Generated by Django 2.2.6 on 2020-05-27 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200527_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Student_id',
            field=models.IntegerField(default=1, unique=True, verbose_name='id'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.0.1 on 2018-02-01 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodspark', '0020_auto_20180201_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='imgurl',
        ),
    ]

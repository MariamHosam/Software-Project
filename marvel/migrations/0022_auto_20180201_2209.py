# Generated by Django 2.0.1 on 2018-02-01 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodspark', '0021_remove_restaurant_imgurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(null=True, upload_to='./uploads'),
        ),
    ]
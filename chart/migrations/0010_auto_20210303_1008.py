# Generated by Django 3.1.7 on 2021-03-03 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0009_auto_20210303_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]

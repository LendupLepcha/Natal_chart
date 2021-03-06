# Generated by Django 3.1.7 on 2021-03-01 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0005_auto_20210219_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat_Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sun', models.FileField(blank=True, default='default.png', upload_to='')),
                ('moon', models.FileField(blank=True, default='default.png', upload_to='')),
                ('mercury', models.FileField(blank=True, default='default.png', upload_to='')),
                ('venus', models.FileField(blank=True, default='default.png', upload_to='')),
                ('mars', models.FileField(blank=True, default='default.png', upload_to='')),
                ('jupiter', models.FileField(blank=True, default='default.png', upload_to='')),
                ('saturn', models.FileField(blank=True, default='default.png', upload_to='')),
                ('uranus', models.FileField(blank=True, default='default.png', upload_to='')),
                ('neptune', models.FileField(blank=True, default='default.png', upload_to='')),
                ('pluto', models.FileField(blank=True, default='default.png', upload_to='')),
                ('ceres', models.FileField(blank=True, default='default.png', upload_to='')),
                ('chart_frame', models.FileField(blank=True, default='default.png', upload_to='')),
                ('aspact_frame', models.FileField(blank=True, default='default.png', upload_to='')),
                ('conjunction', models.FileField(blank=True, default='default.png', upload_to='')),
                ('opposition', models.FileField(blank=True, default='default.png', upload_to='')),
                ('square', models.FileField(blank=True, default='default.png', upload_to='')),
                ('sextile', models.FileField(blank=True, default='default.png', upload_to='')),
                ('trine', models.FileField(blank=True, default='default.png', upload_to='')),
                ('ids', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='user_info',
            name='aspect_grid',
            field=models.FileField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='natal_chart',
            field=models.FileField(blank=True, default='default.png', upload_to=''),
        ),
    ]

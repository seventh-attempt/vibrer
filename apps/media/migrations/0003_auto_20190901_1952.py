# Generated by Django 2.2.4 on 2019-09-01 19:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('media', '0002_auto_20190830_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='file',
            field=models.FileField(default=None, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(default=None, upload_to='media/',
                                    width_field=100),
        ),
    ]

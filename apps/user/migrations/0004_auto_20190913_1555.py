# Generated by Django 2.2.4 on 2019-09-13 15:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0003_auto_20190912_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True,
                                       verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(related_name='users', to='user.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='liked_songs',
            field=models.ManyToManyField(related_name='users',
                                         to='media.Song'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='user',
            name='playlists',
            field=models.ManyToManyField(related_name='users',
                                         to='user.Playlist'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

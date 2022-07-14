# Generated by Django 3.2.4 on 2022-07-12 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0008_auto_20220712_0033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='movies',
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', through='moviedb.Role', to='moviedb.Actor'),
        ),
    ]
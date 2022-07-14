# Generated by Django 3.2.4 on 2022-07-11 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='roles',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='roles',
        ),
        migrations.AddField(
            model_name='actor',
            name='name',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='movie',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(related_name='actors', through='moviedb.Role', to='moviedb.Movie'),
        ),
        migrations.AlterField(
            model_name='role',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='moviedb.actor'),
        ),
        migrations.AlterField(
            model_name='role',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='moviedb.movie'),
        ),
    ]
# Generated by Django 3.2.4 on 2022-07-14 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='author',
            new_name='user',
        ),
    ]

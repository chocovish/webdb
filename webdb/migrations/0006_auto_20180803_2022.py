# Generated by Django 2.1 on 2018-08-03 14:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webdb', '0005_auto_20180802_2300'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='comment',
            new_name='CommentModel',
        ),
        migrations.RenameModel(
            old_name='item',
            new_name='ItemModel',
        ),
        migrations.RenameModel(
            old_name='rating',
            new_name='RatingModel',
        ),
    ]

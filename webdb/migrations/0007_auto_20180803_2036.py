# Generated by Django 2.1 on 2018-08-03 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdb', '0006_auto_20180803_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmodel',
            name='rating',
            field=models.SmallIntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='ratingmodel',
            name='rating',
            field=models.SmallIntegerField(default=5),
        ),
    ]

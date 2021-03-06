# Generated by Django 2.1 on 2018-08-03 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdb', '0009_auto_20180804_0047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratingmodel',
            name='item',
        ),
        migrations.AddField(
            model_name='ratingmodel',
            name='itempk',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='ratingmodel',
            name='rating',
            field=models.SmallIntegerField(default=0),
        ),
    ]

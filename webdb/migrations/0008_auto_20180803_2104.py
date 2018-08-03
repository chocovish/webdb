# Generated by Django 2.1 on 2018-08-03 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdb', '0007_auto_20180803_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmodel',
            name='ratingcount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]

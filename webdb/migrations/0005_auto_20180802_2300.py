# Generated by Django 2.1 on 2018-08-02 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdb', '0004_auto_20180730_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenreList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='genre',
        ),
        migrations.AddField(
            model_name='item',
            name='genre',
            field=models.ManyToManyField(to='webdb.GenreList'),
        ),
    ]

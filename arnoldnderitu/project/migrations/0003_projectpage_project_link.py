# Generated by Django 3.1.2 on 2020-10-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20201016_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='project_link',
            field=models.CharField(default='None', max_length=250),
        ),
    ]

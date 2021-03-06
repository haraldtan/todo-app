# Generated by Django 2.2.7 on 2019-12-28 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_archiveditem'),
    ]

    operations = [
        migrations.AddField(
            model_name='archiveditem',
            name='info',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='archiveditem',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='info',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

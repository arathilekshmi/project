# Generated by Django 4.0.3 on 2022-04-01 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1996-02-08'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2 on 2021-05-05 05:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20210504_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='Add_only_Textfield',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2021, 5, 5, 5, 30, 21, 568369, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice3',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice4',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]

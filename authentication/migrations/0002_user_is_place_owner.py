# Generated by Django 2.1.1 on 2018-09-29 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_place_owner',
            field=models.BooleanField(default=False),
        ),
    ]

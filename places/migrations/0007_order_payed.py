# Generated by Django 2.1.1 on 2018-09-19 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payed',
            field=models.BooleanField(default=False),
        ),
    ]
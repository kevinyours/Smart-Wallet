# Generated by Django 2.2 on 2019-04-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_auto_20190429_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='tx_hash',
            field=models.CharField(max_length=66),
        ),
    ]

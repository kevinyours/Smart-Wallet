# Generated by Django 2.2 on 2019-04-23 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_auto_20190423_0239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterField(
            model_name='wallet',
            name='address',
            field=models.CharField(max_length=42, unique=True),
        ),
    ]

# Generated by Django 3.2.11 on 2022-01-06 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0004_auto_20200417_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributeprovider',
            name='name',
            field=models.CharField(help_text='', max_length=256),
        ),
        migrations.AlterField(
            model_name='attributeprovider',
            name='url',
            field=models.CharField(help_text='', max_length=512),
        ),
    ]
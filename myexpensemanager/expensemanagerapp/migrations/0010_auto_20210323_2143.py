# Generated by Django 3.1.7 on 2021-03-23 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensemanagerapp', '0009_auto_20210323_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fcm_token',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='image_url',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-21 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensemanagerapp', '0004_auto_20210321_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensemanagerapp', '0017_auto_20210325_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

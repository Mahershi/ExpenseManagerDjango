# Generated by Django 3.1.7 on 2021-03-25 18:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('expensemanagerapp', '0019_cluster_last_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='last_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

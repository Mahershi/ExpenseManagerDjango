# Generated by Django 3.1.7 on 2021-03-23 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensemanagerapp', '0008_auto_20210323_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='batch_id',
            new_name='cluster_id',
        ),
    ]
# Generated by Django 5.1.2 on 2024-10-29 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset_app', '0005_rename_taggeddatasets_datasettag_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='is_active',
        ),
        migrations.AddField(
            model_name='datasettag',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
# Generated by Django 5.1.2 on 2024-10-28 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset_app', '0002_remove_tag_dataset_dataset_tags_alter_tag_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='state',
            field=models.BooleanField(),
        ),
    ]
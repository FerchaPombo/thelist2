# Generated by Django 5.0 on 2023-12-15 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_list_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='status',
            new_name='done',
        ),
    ]
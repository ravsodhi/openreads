# Generated by Django 3.0.5 on 2020-04-17 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserGroups', '0005_remove_usergroup_group_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupshelf',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]

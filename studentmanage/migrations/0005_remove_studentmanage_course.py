# Generated by Django 3.2.9 on 2021-12-30 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentmanage', '0004_rename_studentid_studentmanage_studentid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentmanage',
            name='course',
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-27 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='creation_at',
            new_name='created_at',
        ),
    ]

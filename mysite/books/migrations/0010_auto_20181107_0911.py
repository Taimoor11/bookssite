# Generated by Django 2.0.5 on 2018-11-07 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20181107_0907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='activie',
            new_name='active',
        ),
    ]
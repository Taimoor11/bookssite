# Generated by Django 2.0.5 on 2018-11-22 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20181122_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='rating',
        ),
    ]
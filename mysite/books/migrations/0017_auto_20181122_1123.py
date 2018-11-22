# Generated by Django 2.0.5 on 2018-11-22 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_auto_20181122_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='rating',
            field=models.PositiveIntegerField(choices=[(1, '★☆☆☆☆☆☆☆☆☆'), (2, '★★☆☆☆☆☆☆☆☆'), (3, '★★★☆☆☆☆☆☆☆'), (4, '★★★★☆☆☆☆☆☆'), (5, '★★★★★☆☆☆☆☆'), (6, '★★★★★★☆☆☆☆'), (7, '★★★★★★★☆☆☆'), (8, '★★★★★★★★☆☆'), (9, '★★★★★★★★★☆'), (10, '★★★★★★★★★★')], default='1', null=True, verbose_name='Rating'),
        ),
    ]

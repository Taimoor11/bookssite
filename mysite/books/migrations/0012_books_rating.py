# Generated by Django 2.0.5 on 2018-11-22 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20181116_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='rating',
            field=models.PositiveIntegerField(choices=[(1, '★☆☆☆☆☆☆☆☆☆'), (2, '★★☆☆☆☆☆☆☆☆'), (3, '★★★☆☆☆☆☆☆☆'), (4, '★★★★☆☆☆☆☆☆'), (5, '★★★★★☆☆☆☆☆'), (6, '★★★★★★☆☆☆☆'), (7, '★★★★★★★☆☆☆'), (8, '★★★★★★★★☆☆'), (9, '★★★★★★★★★☆'), (10, '★★★★★★★★★★')], default='★☆☆☆☆☆☆☆☆☆', verbose_name='Rating'),
        ),
    ]

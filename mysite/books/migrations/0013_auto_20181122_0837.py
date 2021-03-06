# Generated by Django 2.0.5 on 2018-11-22 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_books_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='rating',
            field=models.PositiveIntegerField(choices=[(1, '★☆☆☆☆☆☆☆☆☆'), (2, '★★☆☆☆☆☆☆☆☆'), (3, '★★★☆☆☆☆☆☆☆'), (4, '★★★★☆☆☆☆☆☆'), (5, '★★★★★☆☆☆☆☆'), (6, '★★★★★★☆☆☆☆'), (7, '★★★★★★★☆☆☆'), (8, '★★★★★★★★☆☆'), (9, '★★★★★★★★★☆'), (10, '★★★★★★★★★★')], default=1, verbose_name='Rating'),
        ),
    ]

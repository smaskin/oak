# Generated by Django 2.1.1 on 2018-10-04 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20180906_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=8, verbose_name='цена'),
        ),
    ]

# Generated by Django 2.1.1 on 2018-09-20 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20180920_0627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='prs',
            new_name='product',
        ),
    ]

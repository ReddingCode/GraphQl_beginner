# Generated by Django 4.1.3 on 2022-11-03 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='tittle',
            new_name='title',
        ),
    ]

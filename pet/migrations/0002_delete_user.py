# Generated by Django 4.1.6 on 2023-04-23 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
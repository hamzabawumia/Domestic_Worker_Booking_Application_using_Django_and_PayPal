# Generated by Django 3.0.5 on 2020-11-18 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20201118_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitter',
            name='rate',
        ),
    ]
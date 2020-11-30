# Generated by Django 3.0.5 on 2020-11-18 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20201118_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='sitter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Sitter'),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

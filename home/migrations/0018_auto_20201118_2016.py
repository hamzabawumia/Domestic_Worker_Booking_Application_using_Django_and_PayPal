# Generated by Django 3.0.5 on 2020-11-18 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20201118_1959'),
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
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]

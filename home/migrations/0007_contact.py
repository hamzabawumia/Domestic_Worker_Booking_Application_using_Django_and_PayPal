# Generated by Django 3.0.5 on 2020-11-11 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_bookingdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('mobile_no', models.CharField(max_length=12)),
                ('service', models.CharField(max_length=122)),
                ('message', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
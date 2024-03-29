# Generated by Django 3.0.5 on 2020-11-11 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_sitter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitter',
            old_name='address1',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='sitter',
            old_name='address2',
            new_name='job',
        ),
        migrations.RenameField(
            model_name='sitter',
            old_name='anymore',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='sitter',
            old_name='phone',
            new_name='religion',
        ),
        migrations.RenameField(
            model_name='sitter',
            old_name='skills',
            new_name='zipcode',
        ),
        migrations.RemoveField(
            model_name='sitter',
            name='aadhar',
        ),
        migrations.RemoveField(
            model_name='sitter',
            name='zipc',
        ),
        migrations.AddField(
            model_name='sitter',
            name='aadhar_card',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='city',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='email',
            field=models.EmailField(max_length=150),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='fname',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='lname',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='pan_card',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='password',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]

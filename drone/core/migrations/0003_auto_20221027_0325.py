# Generated by Django 3.1.7 on 2022-10-27 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20221027_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='serial_number',
            field=models.CharField(default=3, max_length=100),
            preserve_default=False,
        ),
    ]
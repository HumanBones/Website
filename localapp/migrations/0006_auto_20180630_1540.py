# Generated by Django 2.0.2 on 2018-06-30 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localapp', '0005_auto_20180630_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='media/'),
        ),
    ]
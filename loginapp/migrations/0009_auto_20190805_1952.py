# Generated by Django 2.2.3 on 2019-08-05 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0008_auto_20190805_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='botextension',
        ),
        migrations.RemoveField(
            model_name='login',
            name='botpath',
        ),
        migrations.AlterField(
            model_name='login',
            name='college',
            field=models.TextField(max_length=500),
        ),
    ]

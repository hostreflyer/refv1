# Generated by Django 2.0.7 on 2018-07-17 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0003_auto_20180717_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='flight_no',
            field=models.CharField(max_length=25),
        ),
    ]

# Generated by Django 4.1 on 2022-08-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(blank=True, max_length=264),
        ),
    ]

# Generated by Django 2.2.16 on 2021-09-15 15:25

import reviews.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20210915_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(validators=[reviews.models.year_validator], verbose_name='year'),
        ),
    ]

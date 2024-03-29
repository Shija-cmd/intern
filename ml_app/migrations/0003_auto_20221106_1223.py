# Generated by Django 3.2.15 on 2022-11-06 12:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml_app', '0002_data_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='GPA',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='data',
            name='Probability',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='data',
            name='Problem_Statement',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='data',
            name='Recommendation_Letter',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='data',
            name='TOEFL',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]

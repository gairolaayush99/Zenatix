# Generated by Django 3.2.9 on 2021-11-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eval1', '0009_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='item',
            field=models.TextField(max_length=100, unique=True),
        ),
    ]

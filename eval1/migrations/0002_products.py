# Generated by Django 3.2.9 on 2021-11-25 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eval1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=100)),
                ('ingredients', models.TextField(max_length=100)),
                ('price', models.IntegerField()),
                ('weight', models.FloatField()),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-04 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

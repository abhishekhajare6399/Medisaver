# Generated by Django 4.1.7 on 2023-04-08 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0057_alter_appointment_mid_alter_appointment_sid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='mid',
            field=models.IntegerField(default=712820, unique=True),
        ),
        migrations.AlterField(
            model_name='medical_store',
            name='sid',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='mid',
            field=models.IntegerField(default=33396, unique=True),
        ),
    ]
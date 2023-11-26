# Generated by Django 4.1.7 on 2023-04-07 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0037_appointment_order_alter_customuser_cid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='Aid',
            field=models.IntegerField(default=14375387, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cid',
            field=models.IntegerField(default=23200, unique=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='mid',
            field=models.IntegerField(default=409371, unique=True),
        ),
        migrations.AlterField(
            model_name='medical_store',
            name='sid',
            field=models.IntegerField(default=41495, unique=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='mid',
            field=models.IntegerField(default=70346, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='oid',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

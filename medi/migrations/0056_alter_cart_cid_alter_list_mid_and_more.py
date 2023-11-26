# Generated by Django 4.1.7 on 2023-04-07 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0055_alter_appointment_cid_alter_cart_mid_alter_lab_cid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cid',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='list',
            name='mid',
            field=models.IntegerField(default=455170, unique=True),
        ),
        migrations.AlterField(
            model_name='medical_store',
            name='sid',
            field=models.IntegerField(default=84389, unique=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='mid',
            field=models.IntegerField(default=63776, unique=True),
        ),
    ]
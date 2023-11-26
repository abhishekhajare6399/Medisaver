# Generated by Django 4.1.7 on 2023-04-07 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0032_cart_order_alter_customuser_cid_alter_list_mid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cid',
            field=models.IntegerField(default=43103, unique=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='mid',
            field=models.IntegerField(default=275241, unique=True),
        ),
        migrations.AlterField(
            model_name='medical_store',
            name='sid',
            field=models.IntegerField(default=70268, unique=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='mid',
            field=models.IntegerField(default=16989, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='oid',
            field=models.IntegerField(default=14513574, unique=True),
        ),
    ]
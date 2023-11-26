# Generated by Django 4.1.7 on 2023-04-07 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0035_cart_order_alter_customuser_cid_alter_list_mid_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cid',
            field=models.IntegerField(default=27381, unique=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='mid',
            field=models.IntegerField(default=938890, unique=True),
        ),
        migrations.AlterField(
            model_name='medical_store',
            name='sid',
            field=models.IntegerField(default=50852, unique=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='mid',
            field=models.IntegerField(default=84360, unique=True),
        ),
    ]
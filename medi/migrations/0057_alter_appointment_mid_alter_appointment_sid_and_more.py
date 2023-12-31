# Generated by Django 4.1.7 on 2023-04-07 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0056_alter_cart_cid_alter_list_mid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='mid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='sid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cart',
            name='sid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='lab',
            name='mid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='lab',
            name='sid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='list',
            name='mid',
            field=models.IntegerField(default=240524, unique=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='sid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='medical_store',
            name='sid',
            field=models.IntegerField(default=65222, unique=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='mid',
            field=models.IntegerField(default=22521, unique=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='sid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='mid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='sid',
            field=models.CharField(max_length=50),
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-07 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0031_delete_cart_delete_order_alter_customuser_cid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('sid', models.IntegerField()),
                ('mid', models.IntegerField()),
                ('medicine', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oid', models.IntegerField(default=3686196)),
                ('cid', models.IntegerField()),
                ('sid', models.IntegerField()),
                ('mid', models.IntegerField()),
                ('medicine', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('total', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cid',
            field=models.IntegerField(default=18397),
        ),
        migrations.AlterField(
            model_name='list',
            name='mid',
            field=models.IntegerField(default=916646),
        ),
        migrations.AlterField(
            model_name='medical_store',
            name='sid',
            field=models.IntegerField(default=23559),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='mid',
            field=models.IntegerField(default=16070),
        ),
    ]
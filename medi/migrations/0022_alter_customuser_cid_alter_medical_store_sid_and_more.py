# Generated by Django 4.1.7 on 2023-04-05 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0021_alter_customuser_cid_alter_medical_store_sid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cid',
            field=models.IntegerField(default=53324),
        ),
        migrations.AlterField(
            model_name='medical_store',
            name='sid',
            field=models.IntegerField(default=72551),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='mid',
            field=models.IntegerField(default=13977),
        ),
    ]
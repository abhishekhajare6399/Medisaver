# Generated by Django 4.1.7 on 2023-04-05 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0025_alter_customuser_cid_alter_customuser_cpassword_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cid',
            field=models.IntegerField(default=71537),
        ),
        migrations.AlterField(
            model_name='medical_store',
            name='sid',
            field=models.IntegerField(default=92403),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='mid',
            field=models.IntegerField(default=80947),
        ),
    ]

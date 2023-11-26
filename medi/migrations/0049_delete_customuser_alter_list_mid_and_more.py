# Generated by Django 4.1.7 on 2023-04-07 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0048_appointment_lab_alter_customuser_cid_alter_list_mid_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.AlterField(
            model_name='list',
            name='mid',
            field=models.IntegerField(default=186412, unique=True),
        ),
        migrations.AlterField(
            model_name='medical_store',
            name='sid',
            field=models.IntegerField(default=34586, unique=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='mid',
            field=models.IntegerField(default=34214, unique=True),
        ),
    ]
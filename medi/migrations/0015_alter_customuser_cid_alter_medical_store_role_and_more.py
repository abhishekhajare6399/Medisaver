# Generated by Django 4.1.7 on 2023-04-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0014_medical_store_delete_storeuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cid',
            field=models.IntegerField(default=41648),
        ),
        migrations.AlterField(
            model_name='medical_store',
            name='role',
            field=models.CharField(choices=[('MS', 'Medical'), ('HS', 'Hospital'), ('LS', 'Labs')], max_length=2),
        ),
        migrations.AlterField(
            model_name='medical_store',
            name='sid',
            field=models.IntegerField(default=37623),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='mid',
            field=models.IntegerField(default=21369),
        ),
    ]

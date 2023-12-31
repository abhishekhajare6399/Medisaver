# Generated by Django 4.1.7 on 2023-04-07 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0053_alter_customuser_cid_alter_list_mid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cid',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(upload_to='profile/'),
        ),
        migrations.AlterField(
            model_name='list',
            name='image',
            field=models.ImageField(upload_to='Hospital/'),
        ),
        migrations.AlterField(
            model_name='list',
            name='mid',
            field=models.IntegerField(default=700904, unique=True),
        ),
        migrations.AlterField(
            model_name='medical_store',
            name='sid',
            field=models.IntegerField(default=43530, unique=True),
        ),
        migrations.AlterField(
            model_name='medical_store',
            name='store_image',
            field=models.ImageField(upload_to='Store/'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='medicine_image',
            field=models.ImageField(upload_to='Medicine/'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='mid',
            field=models.IntegerField(default=87214, unique=True),
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-04 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0012_alter_customuser_cid_alter_customuser_cpassword_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.IntegerField(default=31134)),
                ('cid', models.IntegerField()),
                ('medicine', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discount', models.FloatField()),
                ('description', models.TextField()),
                ('medicine_status', models.CharField(max_length=10)),
                ('medicine_image', models.ImageField(upload_to='Medicine')),
            ],
        ),
        migrations.CreateModel(
            name='StoreUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('MS', 'Medical Store'), ('HS', 'Hospital'), ('LS', 'Labs')], max_length=2)),
                ('sid', models.IntegerField(default=16634)),
                ('medical_name', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('cpassword', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=254)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('discount', models.FloatField()),
                ('status', models.CharField(max_length=10)),
                ('store_image', models.ImageField(upload_to='Store')),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cid',
            field=models.IntegerField(default=64699),
        ),
    ]

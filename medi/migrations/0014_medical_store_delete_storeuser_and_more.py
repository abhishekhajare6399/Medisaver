# Generated by Django 4.1.7 on 2023-04-04 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0013_medicine_storeuser_alter_customuser_cid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medical_Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('MS', 'Medical Store'), ('HS', 'Hospital'), ('LS', 'Labs')], max_length=2)),
                ('sid', models.IntegerField(default=14019)),
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
        migrations.DeleteModel(
            name='StoreUser',
        ),
        migrations.RenameField(
            model_name='medicine',
            old_name='cid',
            new_name='sid',
        ),
        migrations.RenameField(
            model_name='medicine',
            old_name='medicine_status',
            new_name='status_medicine',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cid',
            field=models.IntegerField(default=78129),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='mid',
            field=models.IntegerField(default=23422),
        ),
    ]
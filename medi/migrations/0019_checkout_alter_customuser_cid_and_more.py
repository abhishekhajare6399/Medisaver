# Generated by Django 4.1.7 on 2023-04-05 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0018_alter_customuser_cid_alter_medical_store_sid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('mid', models.IntegerField()),
                ('price', models.FloatField()),
                ('discount', models.FloatField()),
                ('quantity', models.FloatField()),
                ('total', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cid',
            field=models.IntegerField(default=28478),
        ),
        migrations.AlterField(
            model_name='medical_store',
            name='sid',
            field=models.IntegerField(default=88485),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='mid',
            field=models.IntegerField(default=88478),
        ),
    ]
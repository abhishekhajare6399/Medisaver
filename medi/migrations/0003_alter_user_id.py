# Generated by Django 4.1.7 on 2023-04-04 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0002_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

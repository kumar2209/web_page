# Generated by Django 2.1.3 on 2019-03-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190309_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_detail',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
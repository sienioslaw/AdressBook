# Generated by Django 3.2.7 on 2021-09-26 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0002_auto_20210926_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='postcode',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=100),
        ),
    ]
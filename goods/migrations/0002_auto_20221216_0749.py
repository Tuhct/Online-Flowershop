# Generated by Django 3.0.4 on 2022-12-15 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowerscategory',
            name='cag_css',
            field=models.CharField(max_length=200),
        ),
    ]

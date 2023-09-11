# Generated by Django 3.0.4 on 2022-12-11 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flowersCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cag_name', models.CharField(max_length=30)),
                ('cag_css', models.CharField(max_length=20)),
                ('cag_img', models.ImageField(upload_to='cag')),
            ],
        ),
        migrations.CreateModel(
            name='flowerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flower_name', models.CharField(max_length=100, verbose_name='商品名')),
                ('flower_price', models.IntegerField(default=0, verbose_name='价格')),
                ('flower_desc', models.CharField(max_length=2000, verbose_name='介绍')),
                ('flower_img', models.ImageField(upload_to='flower', verbose_name='图像')),
                ('flower_cag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.flowersCategory')),
            ],
        ),
    ]
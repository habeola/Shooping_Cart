# Generated by Django 2.1 on 2019-10-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20191018_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(default=20, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default=2, upload_to='images/'),
            preserve_default=False,
        ),
    ]
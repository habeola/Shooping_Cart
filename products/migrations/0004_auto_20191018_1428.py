# Generated by Django 2.1 on 2019-10-18 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20191018_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productes', to='products.Item'),
        ),
    ]

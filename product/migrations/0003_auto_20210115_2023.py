# Generated by Django 3.1.5 on 2021-01-15 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.menu'),
        ),
    ]
# Generated by Django 3.1.5 on 2021-01-16 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210115_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcolorimage',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productcolorimages', to='product.image'),
        ),
    ]
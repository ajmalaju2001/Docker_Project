# Generated by Django 4.1 on 2022-10-05 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0026_alter_order_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

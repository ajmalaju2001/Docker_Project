# Generated by Django 4.1 on 2022-09-27 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_alter_product_product_image_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_offer',
            field=models.IntegerField(null=True),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-11 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_ram_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='des',
            field=models.TextField(),
        ),
    ]

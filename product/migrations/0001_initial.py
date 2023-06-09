# Generated by Django 4.2.1 on 2023-06-06 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Ram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('des', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('discount', models.SmallIntegerField()),
                ('image', models.ImageField(upload_to='product')),
                ('color', models.ManyToManyField(related_name='products', to='product.color')),
                ('ram', models.ManyToManyField(related_name='products', to='product.ram')),
                ('storage', models.ManyToManyField(related_name='products', to='product.storage')),
            ],
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-20 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('stock', models.IntegerField(default=0)),
                ('purchase_price', models.FloatField(default=0.0)),
                ('sell_price', models.FloatField(default=0.0)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='products.Category')),
            ],
        ),
    ]

# Generated by Django 3.2.1 on 2022-03-17 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20220315_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
                ('zipcode', models.CharField(max_length=200, null=True)),
                ('message', models.CharField(max_length=1000, null=True)),
                ('number', models.IntegerField(blank=True, default=0, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('dateAdded', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.client')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.order')),
            ],
        ),
    ]

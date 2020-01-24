# Generated by Django 3.0.2 on 2020-01-24 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Customer_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('Order_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Category', models.CharField(max_length=50)),
                ('Condition', models.CharField(max_length=50)),
                ('Price', models.IntegerField()),
                ('Quantity', models.ManyToManyField(blank=True, related_name='customers', to='ModelRelationship.Customer')),
            ],
        ),
    ]
# Generated by Django 3.2 on 2022-06-06 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('BUY', 'BUY'), ('SELL', 'SELL')], max_length=10)),
                ('no_of_stocks', models.IntegerField()),
                ('price_of_stock', models.DecimalField(decimal_places=2, max_digits=7)),
                ('transaction_date', models.DateField()),
                ('stock_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.company')),
            ],
        ),
    ]
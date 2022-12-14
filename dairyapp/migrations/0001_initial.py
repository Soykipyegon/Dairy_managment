

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_address', models.CharField(max_length=100)),
                ('customer_contact', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='feederProduct',
            fields=[
                ('feederProduct_id', models.AutoField(primary_key=True, serialize=False)),
                ('feederProduct_name', models.CharField(max_length=25)),
                ('feederProduct_qtyunit', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='mProduct',
            fields=[
                ('mProduct_id', models.AutoField(primary_key=True, serialize=False)),
                ('mProduct_name', models.CharField(max_length=50)),
                ('mProduct_qty', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='mProductSell',
            fields=[
                ('mProductSell_id', models.AutoField(primary_key=True, serialize=False)),
                ('buyer_name', models.CharField(default='TBD', max_length=50)),
                ('mProductSell_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('mProductSell_qty', models.FloatField()),
                ('mProductSell_qtyunit', models.CharField(default='TBD', max_length=10)),
                ('mProductSell_rate', models.FloatField()),
                ('mProductSell_amount', models.FloatField(default=0)),
                ('milk_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dairyapp.mProduct')),
            ],
        ),
        migrations.CreateModel(
            name='mProductUnit',
            fields=[
                ('mProductUnit_id', models.AutoField(primary_key=True, serialize=False)),
                ('mProductUnit_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='mPurchase',
            fields=[
                ('mPurchase_id', models.AutoField(primary_key=True, serialize=False)),
                ('seller', models.CharField(max_length=50)),
                ('mPurchase_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('mPurchase_product', models.CharField(choices=[('Cow Milk', 'Cow'), ('Buffalo Milk', 'Buffalo')], max_length=15)),
                ('mPurchase_qty', models.FloatField()),
                ('mPurchase_rate', models.FloatField()),
                ('mPurchase_total', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='mStock',
            fields=[
                ('mStock_id', models.AutoField(primary_key=True, serialize=False)),
                ('mStock_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('mStock_qty', models.FloatField()),
                ('mStock_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dairyapp.mProduct')),
            ],
        ),
        migrations.CreateModel(
            name='operationCost',
            fields=[
                ('operationCost_id', models.AutoField(primary_key=True, serialize=False)),
                ('particular', models.CharField(max_length=80)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('qty', models.FloatField()),
                ('rate', models.FloatField()),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='test',
            fields=[
                ('test_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='mproduct',
            name='mProduct_qtyunit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dairyapp.mProductUnit'),
        ),
    ]

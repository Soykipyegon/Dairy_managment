

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0002_auto_20181220_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mproductsell',
            name='mProductSell_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='operationcost',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]

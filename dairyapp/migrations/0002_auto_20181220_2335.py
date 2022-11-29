

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpurchase',
            name='mPurchase_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

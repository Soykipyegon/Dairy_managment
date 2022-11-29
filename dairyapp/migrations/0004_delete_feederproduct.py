

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0003_auto_20181221_0041'),
    ]

    operations = [
        migrations.DeleteModel(
            name='feederProduct',
        ),
    ]

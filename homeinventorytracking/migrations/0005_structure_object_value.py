# Generated by Django 2.1.7 on 2019-03-22 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeinventorytracking', '0004_auto_20190322_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='structure',
            name='object_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]

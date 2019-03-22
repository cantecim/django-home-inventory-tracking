# Generated by Django 2.1.7 on 2019-03-22 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('B', 'Building'), ('A', 'Apartment'), ('R', 'Room')], max_length=1)),
                ('parent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homeinventorytracking.Structure')),
            ],
        ),
        migrations.AddField(
            model_name='object',
            name='structure',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homeinventorytracking.Structure'),
        ),
    ]
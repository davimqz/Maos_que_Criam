# Generated by Django 5.1 on 2024-11-04 11:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app15', '0006_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('consent_to_share', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_type', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField()),
                ('date_donated', models.DateField(auto_now_add=True)),
                ('donor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app15.donor')),
            ],
        ),
    ]

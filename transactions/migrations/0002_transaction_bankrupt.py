# Generated by Django 5.0.6 on 2024-06-15 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='bankrupt',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.0.4 on 2023-05-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_remove_donor_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
    ]

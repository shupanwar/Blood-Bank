# Generated by Django 4.0.4 on 2023-04-30 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
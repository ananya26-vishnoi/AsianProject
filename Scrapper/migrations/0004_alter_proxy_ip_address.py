# Generated by Django 5.0.1 on 2024-01-27 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scrapper', '0003_countriesonline_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxy',
            name='ip_address',
            field=models.CharField(max_length=100),
        ),
    ]
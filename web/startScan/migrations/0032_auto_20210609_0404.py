# Generated by Django 3.1.6 on 2021-06-09 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0031_auto_20210609_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdomain',
            name='ip_addresses',
            field=models.ManyToManyField(related_name='ip_addresses', to='startScan.Ip'),
        ),
    ]

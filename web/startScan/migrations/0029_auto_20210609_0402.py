# Generated by Django 3.1.6 on 2021-06-09 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0028_auto_20210609_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdomain',
            name='ip_addresses',
            field=models.ManyToManyField(related_name='ips', to='startScan.Ip'),
        ),
    ]

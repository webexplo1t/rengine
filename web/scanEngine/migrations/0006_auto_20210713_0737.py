# Generated by Django 3.2.4 on 2021-07-13 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanEngine', '0005_notificationmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationmodel',
            name='send_interesting_notif',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='notificationmodel',
            name='send_new_subdomain_notif',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='notificationmodel',
            name='send_scan_status_notif',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='notificationmodel',
            name='send_vuln_notif',
            field=models.BooleanField(default=True),
        ),
    ]

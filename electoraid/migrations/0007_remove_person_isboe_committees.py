# Generated by Django 3.0 on 2019-12-04 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electoraid', '0006_auto_20191204_0214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='isboe_committees',
        ),
    ]
# Generated by Django 4.1 on 2022-08-12 15:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_billingaddress'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BillingAddress',
            new_name='Address',
        ),
    ]

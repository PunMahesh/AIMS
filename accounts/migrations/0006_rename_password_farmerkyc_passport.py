# Generated by Django 4.1.7 on 2023-04-09 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_farmerkyc_delete_kyc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farmerkyc',
            old_name='Password',
            new_name='Passport',
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-26 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_rename_id_farmerkyc_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerkyc',
            name='BackPic',
            field=models.ImageField(upload_to='images/docs'),
        ),
        migrations.AlterField(
            model_name='farmerkyc',
            name='FrontPic',
            field=models.ImageField(upload_to='images/docs'),
        ),
        migrations.AlterField(
            model_name='farmerkyc',
            name='PassportPhoto',
            field=models.ImageField(upload_to='images/docs'),
        ),
    ]

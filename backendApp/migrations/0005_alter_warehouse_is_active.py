# Generated by Django 4.2.6 on 2024-03-21 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0004_prescriptiondetails_rename_birth_linebot_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

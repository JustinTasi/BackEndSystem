# Generated by Django 4.2.6 on 2024-03-20 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LineBOT',
            fields=[
                ('Line_UID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('ID_card', models.CharField(max_length=100)),
                ('Phone_number', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('Medicine_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Medicine_Name', models.CharField(max_length=100)),
                ('Efficacy', models.TextField()),
                ('Side_Effects', models.TextField()),
                ('Stock_Level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('Prescription_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Date', models.DateField()),
                ('Line_UID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.linebot')),
            ],
        ),
        migrations.CreateModel(
            name='User_Account',
            fields=[
                ('User_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Account', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('Warehouse_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Creation_Date', models.DateField()),
                ('Is_Active', models.BooleanField()),
                ('Medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.medicine')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('Order_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Purchase_date', models.DateField()),
                ('Purchase_Q', models.IntegerField()),
                ('Purchase_unitPrice', models.IntegerField()),
                ('Medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.medicine')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dosage', models.CharField(max_length=100)),
                ('Dispensing_Q', models.IntegerField()),
                ('Medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.medicine')),
                ('Prescriptio_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.prescription')),
            ],
        ),
    ]
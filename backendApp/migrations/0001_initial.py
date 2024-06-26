# Generated by Django 4.2.2 on 2024-05-19 02:07

import backendApp.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('bed_id', models.AutoField(primary_key=True, serialize=False)),
                ('bed_number', models.CharField(blank=True, max_length=5, null=True, unique=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='MainCourse',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=45)),
                ('course_price', models.IntegerField()),
                ('course_image', models.ImageField(blank=True, null=True, upload_to=backendApp.models.course_image_upload_to)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='MealOrderTimeSlot',
            fields=[
                ('timeSlot_id', models.AutoField(primary_key=True, serialize=False)),
                ('timeSlot_name', models.CharField(max_length=3)),
                ('startTime', models.TimeField(default='00:00')),
                ('deadlineTime', models.TimeField(default='00:00')),
                ('endTimes', models.TimeField(default='00:00')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medicine_id', models.AutoField(primary_key=True, serialize=False)),
                ('medicine_name', models.CharField(max_length=100)),
                ('efficacy', models.TextField()),
                ('side_effects', models.TextField()),
                ('min_stock_level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderState',
            fields=[
                ('OrderState_code', models.AutoField(primary_key=True, serialize=False)),
                ('OrderState_name', models.CharField(max_length=10)),
                ('OrderState_htmlStyle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('patient_name', models.CharField(max_length=45)),
                ('patient_birth', models.DateField()),
                ('patient_number', models.CharField(max_length=10)),
                ('patient_idcard', models.CharField(max_length=10)),
                ('line_notify', models.CharField(blank=True, max_length=45, null=True, unique=True)),
                ('line_id', models.CharField(blank=True, max_length=45, null=True, unique=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('prescription_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('barcode', models.CharField(default=uuid.uuid4, editable=False, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sides',
            fields=[
                ('sides_id', models.AutoField(primary_key=True, serialize=False)),
                ('sides_name', models.CharField(max_length=45)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Stocking',
            fields=[
                ('stocking_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=45)),
                ('supplier_number', models.CharField(blank=True, max_length=10, null=True)),
                ('line_notify', models.CharField(blank=True, max_length=45, null=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('warehouse_id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.medicine')),
            ],
        ),
        migrations.CreateModel(
            name='StockingDetail',
            fields=[
                ('stocking_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('stocking_quantity', models.IntegerField()),
                ('stocking_date', models.DateTimeField()),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('sides', models.ForeignKey(db_column='sides_id', on_delete=django.db.models.deletion.CASCADE, to='backendApp.sides')),
                ('stocking', models.ForeignKey(db_column='stocking_id', on_delete=django.db.models.deletion.CASCADE, to='backendApp.stocking')),
            ],
        ),
        migrations.AddField(
            model_name='stocking',
            name='supplier',
            field=models.ForeignKey(db_column='supplier_id', on_delete=django.db.models.deletion.CASCADE, to='backendApp.supplier'),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_date', models.DateField()),
                ('purchase_q', models.IntegerField()),
                ('purchase_unit_price', models.IntegerField()),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.medicine')),
            ],
        ),
        migrations.CreateModel(
            name='PrescriptionDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosage', models.CharField(max_length=100)),
                ('dispensing_q', models.IntegerField()),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.medicine')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='backendApp.prescription')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_quantity', models.IntegerField()),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(db_column='course_id', on_delete=django.db.models.deletion.CASCADE, to='backendApp.maincourse')),
                ('orderState', models.ForeignKey(db_column='OrderState_code', on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='backendApp.orderstate')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='backendApp.patient')),
            ],
        ),
        migrations.AddField(
            model_name='maincourse',
            name='timeSlot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='backendApp.mealordertimeslot'),
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('delivery_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.SmallIntegerField(default=0)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('bed', models.ForeignKey(db_column='bed_id', on_delete=django.db.models.deletion.CASCADE, to='backendApp.bed')),
                ('order', models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.CASCADE, to='backendApp.order')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSides',
            fields=[
                ('coursesides_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(db_column='course_id', on_delete=django.db.models.deletion.CASCADE, related_name='course_sides', to='backendApp.maincourse')),
                ('sides', models.ForeignKey(db_column='sides_id', on_delete=django.db.models.deletion.CASCADE, to='backendApp.sides')),
            ],
        ),
        migrations.AddField(
            model_name='bed',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backendApp.patient'),
        ),
    ]

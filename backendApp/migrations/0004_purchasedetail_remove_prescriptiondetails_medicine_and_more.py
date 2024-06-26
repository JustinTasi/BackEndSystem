# Generated by Django 4.2.2 on 2024-05-22 00:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0003_alter_coursesides_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseDetail',
            fields=[
                ('purchase_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_quantity', models.IntegerField()),
                ('purchase_date', models.DateTimeField()),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='prescriptiondetails',
            name='medicine',
        ),
        migrations.RemoveField(
            model_name='prescriptiondetails',
            name='prescription',
        ),
        migrations.RemoveField(
            model_name='stocking',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='stockingdetail',
            name='sides',
        ),
        migrations.RemoveField(
            model_name='stockingdetail',
            name='stocking',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='medicine',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='order_id',
            new_name='purchase_id',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='medicine',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='purchase_date',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='purchase_q',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='purchase_unit_price',
        ),
        migrations.AddField(
            model_name='purchase',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplier',
            field=models.ForeignKey(db_column='supplier_id', default=None, on_delete=django.db.models.deletion.CASCADE, to='backendApp.supplier'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Medicine',
        ),
        migrations.DeleteModel(
            name='PrescriptionDetails',
        ),
        migrations.DeleteModel(
            name='Stocking',
        ),
        migrations.DeleteModel(
            name='StockingDetail',
        ),
        migrations.DeleteModel(
            name='Warehouse',
        ),
        migrations.AddField(
            model_name='purchasedetail',
            name='purchase',
            field=models.ForeignKey(db_column='purchase_id', on_delete=django.db.models.deletion.CASCADE, to='backendApp.purchase'),
        ),
        migrations.AddField(
            model_name='purchasedetail',
            name='sides',
            field=models.ForeignKey(db_column='sides_id', on_delete=django.db.models.deletion.CASCADE, to='backendApp.sides'),
        ),
    ]

# Generated by Django 2.0 on 2017-12-15 08:32

import datetime
import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CbcReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('wbc_tc', models.FloatField()),
                ('wbc_tc_unit', models.CharField(max_length=10)),
                ('rbc_tc', models.FloatField()),
                ('rbc_tc_unit', models.CharField(max_length=10)),
                ('haemoglobin', models.FloatField()),
                ('haemoglobin_unit', models.CharField(max_length=10)),
                ('hct', models.FloatField()),
                ('hct_unit', models.CharField(max_length=10)),
                ('platelets_tc', models.FloatField()),
                ('platelets_unit', models.CharField(max_length=10)),
                ('mcv', models.FloatField()),
                ('mcv_unit', models.CharField(max_length=10)),
                ('mch', models.FloatField()),
                ('mch_unit', models.CharField(max_length=10)),
                ('mchc', models.FloatField()),
                ('mchc_unit', models.CharField(max_length=10)),
                ('neutrophil_tc', models.FloatField()),
                ('neutrophil_tc_unit', models.CharField(max_length=10)),
                ('lymphocyte_tc', models.FloatField()),
                ('lymphocyte_tc_unit', models.CharField(max_length=10)),
                ('monocyte_tc', models.FloatField()),
                ('monocyte_tc_unit', models.CharField(max_length=10)),
                ('eosinophil_tc', models.FloatField()),
                ('eosinophil_tc_unit', models.CharField(max_length=10)),
                ('basophil_tc', models.FloatField()),
                ('basophil_tc_unit', models.CharField(max_length=10)),
                ('neutrophil_dc', models.FloatField()),
                ('lymphocyte_dc', models.FloatField()),
                ('monocyte_dc', models.FloatField()),
                ('eosinophil_dc', models.FloatField()),
                ('basophil_dc', models.FloatField()),
                ('rdw_cv', models.FloatField()),
                ('upload_time', models.DateTimeField(default=datetime.datetime.now)),
                ('location', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='ReferenceRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('age', models.FloatField()),
            ],
        ),
    ]

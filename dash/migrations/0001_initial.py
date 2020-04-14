# Generated by Django 3.0.5 on 2020-04-05 09:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='death',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_update', models.DateTimeField(default=datetime.datetime.now)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('andaman_and_nicobar', models.IntegerField(default=0)),
                ('andhra_pradesh', models.IntegerField(default=0)),
                ('arunachal_pradesh', models.IntegerField(default=0)),
                ('assam', models.IntegerField(default=0)),
                ('bihar', models.IntegerField(default=0)),
                ('chandigarh', models.IntegerField(default=0)),
                ('chhattisgarh', models.IntegerField(default=0)),
                ('daman_n_diu', models.IntegerField(default=0)),
                ('delhi', models.IntegerField(default=0)),
                ('dadra_nagar_haveli', models.IntegerField(default=0)),
                ('goa', models.IntegerField(default=0)),
                ('gujarat', models.IntegerField(default=0)),
                ('himachal_pradesh', models.IntegerField(default=0)),
                ('haryana', models.IntegerField(default=0)),
                ('jharkhand', models.IntegerField(default=0)),
                ('jammu_and_kashmir', models.IntegerField(default=0)),
                ('karnataka', models.IntegerField(default=0)),
                ('kerala', models.IntegerField(default=0)),
                ('lakshadeep', models.IntegerField(default=0)),
                ('ladakh', models.IntegerField(default=0)),
                ('maharashtra', models.IntegerField(default=0)),
                ('meghalaya', models.IntegerField(default=0)),
                ('manipur', models.IntegerField(default=0)),
                ('madhya_pradesh', models.IntegerField(default=0)),
                ('mizoram', models.IntegerField(default=0)),
                ('nagaland', models.IntegerField(default=0)),
                ('odisha', models.IntegerField(default=0)),
                ('punjab', models.IntegerField(default=0)),
                ('puducherry', models.IntegerField(default=0)),
                ('rajasthan', models.IntegerField(default=0)),
                ('sikkim', models.IntegerField(default=0)),
                ('tamil_nadu', models.IntegerField(default=0)),
                ('telangana', models.IntegerField(default=0)),
                ('tripura', models.IntegerField(default=0)),
                ('uttar_pradesh', models.IntegerField(default=0)),
                ('uttarakhand', models.IntegerField(default=0)),
                ('west_bengal', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='deathdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('death_number', models.IntegerField(unique=True)),
                ('death_date', models.DateField()),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('nationality', models.CharField(blank=True, max_length=20, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('suspected_reason', models.CharField(blank=True, max_length=100, null=True)),
                ('comorbidities', models.CharField(blank=True, max_length=100, null=True)),
                ('source', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('person', models.EmailField(max_length=254)),
                ('datetime_update', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='indianabroad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_update', models.DateTimeField(default=datetime.datetime.now)),
                ('country', models.CharField(max_length=100)),
                ('active_cases', models.IntegerField()),
                ('deaths', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='keycountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_update', models.DateTimeField(default=datetime.datetime.now)),
                ('date', models.DateField(default=datetime.date.today)),
                ('china', models.IntegerField()),
                ('us', models.IntegerField()),
                ('uk', models.IntegerField()),
                ('italy', models.IntegerField()),
                ('france', models.IntegerField()),
                ('germany', models.IntegerField()),
                ('spain', models.IntegerField()),
                ('iran', models.IntegerField()),
                ('india', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='newcase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_update', models.DateTimeField(default=datetime.datetime.now)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('andaman_and_nicobar', models.IntegerField(default=0)),
                ('andhra_pradesh', models.IntegerField(default=0)),
                ('arunachal_pradesh', models.IntegerField(default=0)),
                ('assam', models.IntegerField(default=0)),
                ('bihar', models.IntegerField(default=0)),
                ('chandigarh', models.IntegerField(default=0)),
                ('chhattisgarh', models.IntegerField(default=0)),
                ('daman_n_diu', models.IntegerField(default=0)),
                ('delhi', models.IntegerField(default=0)),
                ('dadra_nagar_haveli', models.IntegerField(default=0)),
                ('goa', models.IntegerField(default=0)),
                ('gujarat', models.IntegerField(default=0)),
                ('himachal_pradesh', models.IntegerField(default=0)),
                ('haryana', models.IntegerField(default=0)),
                ('jharkhand', models.IntegerField(default=0)),
                ('jammu_and_kashmir', models.IntegerField(default=0)),
                ('karnataka', models.IntegerField(default=0)),
                ('kerala', models.IntegerField(default=0)),
                ('lakshadeep', models.IntegerField(default=0)),
                ('ladakh', models.IntegerField(default=0)),
                ('maharashtra', models.IntegerField(default=0)),
                ('meghalaya', models.IntegerField(default=0)),
                ('manipur', models.IntegerField(default=0)),
                ('madhya_pradesh', models.IntegerField(default=0)),
                ('mizoram', models.IntegerField(default=0)),
                ('nagaland', models.IntegerField(default=0)),
                ('odisha', models.IntegerField(default=0)),
                ('punjab', models.IntegerField(default=0)),
                ('puducherry', models.IntegerField(default=0)),
                ('rajasthan', models.IntegerField(default=0)),
                ('sikkim', models.IntegerField(default=0)),
                ('tamil_nadu', models.IntegerField(default=0)),
                ('telangana', models.IntegerField(default=0)),
                ('tripura', models.IntegerField(default=0)),
                ('uttar_pradesh', models.IntegerField(default=0)),
                ('uttarakhand', models.IntegerField(default=0)),
                ('west_bengal', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='recovery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_update', models.DateTimeField(default=datetime.datetime.now)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('andaman_and_nicobar', models.IntegerField(default=0)),
                ('andhra_pradesh', models.IntegerField(default=0)),
                ('arunachal_pradesh', models.IntegerField(default=0)),
                ('assam', models.IntegerField(default=0)),
                ('bihar', models.IntegerField(default=0)),
                ('chandigarh', models.IntegerField(default=0)),
                ('chhattisgarh', models.IntegerField(default=0)),
                ('daman_n_diu', models.IntegerField(default=0)),
                ('delhi', models.IntegerField(default=0)),
                ('dadra_nagar_haveli', models.IntegerField(default=0)),
                ('goa', models.IntegerField(default=0)),
                ('gujarat', models.IntegerField(default=0)),
                ('himachal_pradesh', models.IntegerField(default=0)),
                ('haryana', models.IntegerField(default=0)),
                ('jharkhand', models.IntegerField(default=0)),
                ('jammu_and_kashmir', models.IntegerField(default=0)),
                ('karnataka', models.IntegerField(default=0)),
                ('kerala', models.IntegerField(default=0)),
                ('lakshadeep', models.IntegerField(default=0)),
                ('ladakh', models.IntegerField(default=0)),
                ('maharashtra', models.IntegerField(default=0)),
                ('meghalaya', models.IntegerField(default=0)),
                ('manipur', models.IntegerField(default=0)),
                ('madhya_pradesh', models.IntegerField(default=0)),
                ('mizoram', models.IntegerField(default=0)),
                ('nagaland', models.IntegerField(default=0)),
                ('odisha', models.IntegerField(default=0)),
                ('punjab', models.IntegerField(default=0)),
                ('puducherry', models.IntegerField(default=0)),
                ('rajasthan', models.IntegerField(default=0)),
                ('sikkim', models.IntegerField(default=0)),
                ('tamil_nadu', models.IntegerField(default=0)),
                ('telangana', models.IntegerField(default=0)),
                ('tripura', models.IntegerField(default=0)),
                ('uttar_pradesh', models.IntegerField(default=0)),
                ('uttarakhand', models.IntegerField(default=0)),
                ('west_bengal', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='testcount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_update', models.DateTimeField(default=datetime.datetime.now)),
                ('date', models.DateField(default=datetime.date.today)),
                ('test_count', models.IntegerField()),
            ],
        ),
    ]

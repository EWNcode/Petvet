# Generated by Django 2.2.1 on 2019-05-25 19:22

import animals.validators
import common.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, validators=[common.validators.NameValidator()])),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=6)),
                ('kind', models.CharField(choices=[('D', 'Dog'), ('C', 'Cat')], max_length=3)),
                ('birthday', models.DateField()),
                ('serial_number', models.CharField(max_length=10, unique=True, validators=[animals.validators.SerialNumberValidator()])),
                ('general_information', models.TextField(blank=True, null=True)),
                ('vaccine_1', models.BooleanField(null=True)),
                ('vaccine_1_date', models.DateField(null=True)),
                ('vaccine_2', models.BooleanField(null=True)),
                ('vaccine_2_date', models.DateField(null=True)),
                ('vaccine_3', models.BooleanField(null=True)),
                ('vaccine_3_date', models.DateField(null=True)),
                ('vaccine_4', models.BooleanField(null=True)),
                ('vaccine_4_date', models.DateField(null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

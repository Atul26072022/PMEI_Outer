# Generated by Django 4.1.7 on 2023-06-11 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdi_client', '0003_coilrejectmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleCancellation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specific_coil_no', models.CharField(blank=True, max_length=100, null=True)),
                ('spare', models.CharField(blank=True, max_length=100, null=True)),
                ('read_flag', models.BooleanField(default=False, max_length=100)),
            ],
        ),
    ]

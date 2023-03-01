# Generated by Django 4.1.4 on 2023-02-27 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0005_alter_employee_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email_id',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='hometown',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='employee',
            name='resident_address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='supervisor',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='employee',
            name='surname',
            field=models.CharField(max_length=20),
        ),
    ]

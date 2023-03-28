# Generated by Django 3.2 on 2023-03-28 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0013_employee_salary_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_salary_history',
            name='date',
        ),
        migrations.AddField(
            model_name='employee_salary_history',
            name='month',
            field=models.IntegerField(default=2022),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee_salary_history',
            name='year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

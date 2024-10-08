# Generated by Django 5.1 on 2024-08-09 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0002_initial'),
        ('customuser', '0003_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='assigned_to',
            field=models.ForeignKey(limit_choices_to={'user_type': 'DEV'}, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to='customuser.customuser'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'user_type__in': ['QA', 'MA']}, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='customuser.customuser'),
        ),
    ]

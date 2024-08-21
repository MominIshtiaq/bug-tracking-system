# Generated by Django 5.1 on 2024-08-16 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0007_alter_bug_screenshot'),
        ('projects', '0002_alter_projects_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bugs', to='projects.projects'),
        ),
    ]

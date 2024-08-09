# Generated by Django 5.1 on 2024-08-09 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('screenshot', models.ImageField(blank=True, default='project_bug.jpeg', upload_to='')),
                ('type', models.CharField(choices=[('feature', 'Feature'), ('bug', 'Bug')], max_length=7)),
                ('status', models.CharField(default='new', max_length=10)),
            ],
        ),
    ]

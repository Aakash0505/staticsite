# Generated by Django 3.2.25 on 2024-10-02 10:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0015_alter_file_owner_alter_file_polymorphic_ctype_and_more'),
        ('home', '0003_auto_20241001_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='uploads/Careers/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])]),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Title')),
                ('designation', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Designation')),
                ('published', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('image', filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile_image', to='filer.file')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Team',
            },
        ),
    ]

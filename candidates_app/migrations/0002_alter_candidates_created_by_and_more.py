# Generated by Django 5.0 on 2023-12-09 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidates',
            name='created_by',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='candidates',
            name='modified_by',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-15 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20200215_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='designation',
            field=models.CharField(default='designation', max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='domain',
            field=models.CharField(default='domain', max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='skill_sets',
            field=models.CharField(default='skillsets', max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='working_organization',
            field=models.CharField(default='working_organization', max_length=60),
        ),
    ]

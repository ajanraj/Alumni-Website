# Generated by Django 3.0.2 on 2020-02-14 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='UserName', max_length=50)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
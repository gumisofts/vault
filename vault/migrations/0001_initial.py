# Generated by Django 5.1.6 on 2025-02-15 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_number', models.PositiveBigIntegerField(unique=True)),
                ('dev_mode', models.CharField(choices=[('beta', 'Beta'), ('dev', 'Dev'), ('pro', 'Pro')], max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecretValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('vault', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vault.vault')),
            ],
        ),
    ]

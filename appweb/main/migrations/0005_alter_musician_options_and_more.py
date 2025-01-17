# Generated by Django 5.1.4 on 2025-01-15 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_musician'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='musician',
            options={'ordering': ['-time_create']},
        ),
        migrations.AddIndex(
            model_name='musician',
            index=models.Index(fields=['-time_create'], name='main_musici_time_cr_9653ac_idx'),
        ),
    ]

# Generated by Django 5.0.2 on 2025-03-06 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activitylog',
            options={'ordering': ['-logged_at', '-created_at']},
        ),
        migrations.AlterUniqueTogether(
            name='activitylog',
            unique_together=set(),
        ),
    ]

# Generated by Django 5.1.4 on 2025-01-22 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]

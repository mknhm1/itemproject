# Generated by Django 4.2.6 on 2023-11-30 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadget', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gadgetpost',
            name='map',
            field=models.TextField(blank=True, null=True, verbose_name='マップ'),
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-25 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0020_auto_20210925_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_codes'),
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-25 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0014_auto_20210925_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='availability',
            field=models.CharField(choices=[('да', 'да'), ('нет', 'нет')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='object',
            name='condition',
            field=models.CharField(choices=[('новый', 'новый'), ('б/у', 'б/у')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='object',
            name='employee',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coursework.employee'),
        ),
    ]
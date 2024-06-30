# Generated by Django 3.2.25 on 2024-05-24 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]

# Generated by Django 2.2 on 2024-05-26 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='name_eng',
            field=models.CharField(default='영어이름', max_length=80),
        ),
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]

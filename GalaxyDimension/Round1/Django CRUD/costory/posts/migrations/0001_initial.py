# Generated by Django 2.2 on 2020-10-22 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('dt_created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('dt_modified', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
            ],
        ),
    ]

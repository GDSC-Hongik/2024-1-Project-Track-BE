import coplate.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0002_user_nickname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('restaurant_name', models.CharField(max_length=20)),
                ('restaurant_link', models.URLField(validators=[coplate.validators.validate_rastaurant_link])),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('image1', models.ImageField(upload_to='review_pics')),
                ('image2', models.ImageField(blank=True, upload_to='review_pics')),
                ('image3', models.ImageField(blank=True, upload_to='review_pics')),
                ('content', models.TextField()),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(error_messages={'unique': '이미 사용중인 닉네임입니다.'}, max_length=15, null=True, unique=True, validators=[coplate.validators.validate_no_special_characters]),
        ),
    ]

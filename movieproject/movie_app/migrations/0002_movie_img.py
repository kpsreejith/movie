# Generated by Django 4.2.7 on 2023-11-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='picture', upload_to='gallery'),
            preserve_default=False,
        ),
    ]

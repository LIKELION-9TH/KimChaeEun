# Generated by Django 3.2.2 on 2021-07-31 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0002_hobby_music'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='image',
            field=models.ImageField(blank='True', upload_to='Music/'),
        ),
    ]
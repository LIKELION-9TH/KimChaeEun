# Generated by Django 3.2.2 on 2022-06-26 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='picture',
            field=models.ImageField(blank=True, upload_to='picture/'),
        ),
    ]

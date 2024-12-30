# Generated by Django 5.1.3 on 2024-12-29 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_nav'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_image',
            field=models.ImageField(upload_to='static/profile'),
        ),
        migrations.AlterField(
            model_name='nav',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-29 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='statics/images')),
                ('title', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=100)),
            ],
        ),
    ]
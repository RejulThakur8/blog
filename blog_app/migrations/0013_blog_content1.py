# Generated by Django 5.1.3 on 2025-01-01 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0012_subcategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content1',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]

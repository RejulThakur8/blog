# Generated by Django 5.1.3 on 2025-01-04 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0018_blogcomments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomments',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog_app.blogcomments'),
        ),
    ]

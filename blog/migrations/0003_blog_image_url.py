# Generated by Django 5.0.6 on 2024-07-20 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

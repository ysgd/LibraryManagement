# Generated by Django 5.0.3 on 2024-03-09 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
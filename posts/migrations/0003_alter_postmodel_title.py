# Generated by Django 4.2.6 on 2023-10-06 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_postmodel_photo_postmodel_summary_postmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]

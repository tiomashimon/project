# Generated by Django 4.2.6 on 2023-10-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_postmodel_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='photo',
            field=models.FileField(default='posts/download.png', upload_to='posts/%y/%m/%d/'),
        ),
    ]

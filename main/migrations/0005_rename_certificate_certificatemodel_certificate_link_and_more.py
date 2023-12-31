# Generated by Django 4.2.6 on 2023-10-07 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_lawyermodel_extract'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificatemodel',
            old_name='certificate',
            new_name='certificate_link',
        ),
        migrations.AlterField(
            model_name='lawyermodel',
            name='image',
            field=models.ImageField(upload_to='images/%y/%m/%d'),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-07 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_certificatemodel_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
    ]

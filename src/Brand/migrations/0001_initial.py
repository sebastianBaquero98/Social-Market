# Generated by Django 3.2.5 on 2021-07-30 02:57

import Brand.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='nombre de la marca')),
                ('logo', models.ImageField(blank=True, default=Brand.models.get_default_logo_image_filepath, max_length=255, null=True, upload_to=Brand.models.get_logo_image_filepath)),
            ],
        ),
    ]

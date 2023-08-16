# Generated by Django 4.2.3 on 2023-08-12 16:10

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_careerbanner_careers_testimonial_toppacks_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="careerbanner",
            name="image",
            field=models.ImageField(default="", upload_to=app.models.image_path_rename),
        ),
        migrations.AddField(
            model_name="toppacks",
            name="add_image",
            field=models.ImageField(
                default="", max_length=255, upload_to=app.models.image_path_rename
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="careers",
            name="image",
            field=models.ImageField(upload_to=app.models.image_path_rename),
        ),
    ]

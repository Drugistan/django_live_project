# Generated by Django 4.2.3 on 2023-08-26 18:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0009_remove_topbanner_image_topbannerimages"),
    ]

    operations = [
        migrations.AddField(
            model_name="toppacks",
            name="image_by_title",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
    ]

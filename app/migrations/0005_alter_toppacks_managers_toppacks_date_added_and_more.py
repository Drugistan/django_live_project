# Generated by Django 4.2.3 on 2023-08-12 17:08

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_careerbanner_image_toppacks_add_image_and_more"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="toppacks",
            managers=[
                ("get_active_packs", django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name="toppacks",
            name="date_added",
            field=models.DateTimeField(auto_now_add=True, default="2023-08-12"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="toppacks",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 4.2.3 on 2023-09-05 12:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0013_whychoseus_alter_aboutasserts_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testimonial",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]

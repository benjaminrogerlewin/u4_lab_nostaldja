# Generated by Django 4.1.7 on 2023-03-29 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("nostaldja", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fads",
            name="decade",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="songs",
                to="nostaldja.decade",
            ),
        ),
    ]

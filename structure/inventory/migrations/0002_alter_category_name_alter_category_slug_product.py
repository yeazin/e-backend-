# Generated by Django 4.1.3 on 2022-12-24 15:41

from django.db import migrations, models
import mptt.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                help_text="format: required , max-200",
                max_length=200,
                verbose_name="Category Name",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.CharField(
                help_text="format: required , max-200",
                max_length=200,
                verbose_name="Category Safe URL",
            ),
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        help_text="format: required , max-200",
                        max_length=200,
                        verbose_name="Prodcut Name",
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        help_text="format: required , max-255",
                        max_length=255,
                        verbose_name="Product Safe URL",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Not required",
                        null=True,
                        verbose_name="Product Description",
                    ),
                ),
                ("category", mptt.fields.TreeManyToManyField(to="inventory.category")),
            ],
            options={
                "verbose_name_plural": "Product Table",
            },
        ),
    ]

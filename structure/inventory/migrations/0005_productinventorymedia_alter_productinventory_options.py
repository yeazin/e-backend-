# Generated by Django 4.1.3 on 2022-12-25 13:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0004_brand_producttype_productinventory_brand_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductInventoryMedia",
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
                    "title",
                    models.CharField(
                        help_text="Format : Required",
                        max_length=255,
                        verbose_name="Product Image Title",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        help_text="Format : required",
                        upload_to="images/product/",
                        verbose_name="Product Image",
                    ),
                ),
                (
                    "alt_text",
                    models.CharField(
                        blank=True,
                        help_text="format : Not Required",
                        max_length=100,
                        null=True,
                        verbose_name="Alt Text",
                    ),
                ),
                (
                    "is_featured",
                    models.BooleanField(default=False, verbose_name="Is Featured ?"),
                ),
            ],
            options={
                "verbose_name_plural": "Inventory Images",
            },
        ),
        migrations.AlterModelOptions(
            name="productinventory",
            options={"verbose_name_plural": "Product Inventory"},
        ),
    ]

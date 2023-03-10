# Generated by Django 4.1.3 on 2022-12-25 07:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0003_productinventory"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
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
                        help_text="Format: Required and Unique",
                        max_length=100,
                        unique=True,
                        verbose_name="Product Type",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Brand",
            },
        ),
        migrations.CreateModel(
            name="ProductType",
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
                        help_text="Format: Required and Unique",
                        max_length=100,
                        unique=True,
                        verbose_name="Product Type",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Product Type",
            },
        ),
        migrations.AddField(
            model_name="productinventory",
            name="brand",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="brand",
                to="inventory.brand",
            ),
        ),
        migrations.AddField(
            model_name="productinventory",
            name="product_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="product_type",
                to="inventory.producttype",
            ),
        ),
    ]

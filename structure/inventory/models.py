"""
Inventory Models
"""

from django.db import models
from mainConfig.models.mixin import TimeStampMixin
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


"""
Category models 
"""


class Category(MPTTModel, TimeStampMixin):

    ## Category table implimented with MPTT
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Category Name"),
        help_text=_("format: required , max-200"),
    )
    slug = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Category Safe URL"),
        help_text=_("format: required , max-200"),
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Product Category"),
        help_text=_("Not Required"),
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return str(self.name)

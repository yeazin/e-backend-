from django.db import models
import uuid



class TimeStampMixin(models.Model):
   
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        
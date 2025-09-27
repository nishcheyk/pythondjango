from django.db import models
import uuid

class baseModel(models.Model):
    uid = models.UUIDField(primary_key = True , editable = False , default = uuid.uuid4)
    create_at =models.DateTimeField(auto_now = True)
    update_at = models.DateTimeField(auto_now_add = True)

class meta:
    abstract = True
from django.db import models
from django.contrib.auth.models import User

class AssetQuerySet(models.query.QuerySet):
  def allowed_for_user(self, user):
    return self.filter(owner=user)

class AssetManager(models.Manager):
  use_for_related_fields = True

  def get_query_set(self):
    return AssetQuerySet(self.model)

  def allowed_for_user(self, *args, **kwargs):
    return self.get_query_set().allowed_for_user(*args, **kwargs)

class Asset(models.Model):
  owner = models.ForeignKey(User, related_name='asset_user', verbose_name='Owner')
  objects = AssetManager()
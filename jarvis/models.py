# This is where the models go!
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

# Using the user: user = models.ForeignKey(settings.AUTH_USER_MODEL)
class CodeShare(models.Model):
    md5 = models.CharField(max_length=32)
    code = models.TextField()

    parent = models.ForeignKey('jarvis.CodeShare', null=True, blank=True)

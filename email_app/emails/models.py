from django.db import models
from django.utils.html import escape
from django.utils.safestring import mark_safe

# Create your models here.

class Entity(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, default=None)
    email = models.EmailField(max_length=100, blank=False, null=False, unique=True, default=None)

    @property
    def friendly_name(self):
        return mark_safe(u"%s") % (escape(self.name))

    @property
    def friendly_email(self):
        return mark_safe(u"%s") % (escape(self.email))

    @property
    def name_email(self):
        return mark_safe(u"%s <%s>") % (escape(self.name), escape(self.email))

    def __str__(self):
        return u"name: %s \temail: %s" % (self.friendly_name, self.friendly_email)



def save(self, *args, **kwargs):
    self.email = self.email.lower().strip()
    if (self.email is not None and self.email == ""):
        self.email = None

    self.full_clean()
    super(Entity, self).save(*args, **kwargs)

    #models.Model.save(self, *args, **kwargs)

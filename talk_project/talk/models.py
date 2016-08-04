from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
import re

# Create your models here.
class PostManager(models.Manager):
    def cleanit(self):
        matches = []
        for match in re.finditer(r"\(?[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}/g", request.get['text']):
            clean = re.findall(r'\d+', match.group())
            matches.append(clean)
        new = [''.join([str(b) for b in a]) for a in matches]
        return new

class Post(models.Model):
    author = models.ForeignKey(User)
    text = models.TextField(validators=[MaxLengthValidator(2000)])
    #objects = models.Manager()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def cleanit(self):
        matches = []
        for match in re.finditer(r"\(?[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}/g", "placeholder 1111111111"):
            clean = re.findall(r'\d+', match.group())
            matches.append(clean)
        new = [''.join([str(b) for b in a]) for a in matches]
        return new

    clean_text = cleanit(text)

    def __unicode__(self):
        return self.text+' - '+self.author.username

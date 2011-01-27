from django.db import models
from django.db.models.query import Q

from biblion.exceptions import InvalidSection
from biblion.settings import ALL_SECTION_NAME

class PostManager(models.Manager):
    
    def published(self):
        return self.exclude(published=None)
    
    def current(self):
        return self.published().order_by("-published")
    
    def section(self, value=None, queryset=None):
        
        if queryset is None:
            queryset = self.published()
        
        if value is None or (value == ALL_SECTION_NAME):
            return queryset
        else:
            print queryset.all()
            return queryset.filter(Q(sections__slug=ALL_SECTION_NAME) | Q(sections__slug=value))

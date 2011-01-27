from django.db import models
from django.db.models.query import Q

from biblion.exceptions import InvalidSection
from biblion.settings import ALL_SECTION_NAME

class PostManager(models.Manager):
    
    def published(self):
        return self.exclude(published=None)
    
    def current(self):
        return self.published().order_by("-published")
    
    def section(self, value, queryset=None):
        
        if queryset is None:
            queryset = self.published()
        
        if not value or (value == ALL_SECTION_NAME):
            print queryset
            return queryset
        else:
            print queryset
            a = queryset.filter(Q(sections__slug=ALL_SECTION_NAME) | Q(sections__slug=value))
            print a
            return a
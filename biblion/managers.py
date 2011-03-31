from django.conf import settings
from django.db import models
from django.db.models.query import Q

from biblion.exceptions import InvalidSection
from biblion.settings import ALL_SECTION_NAME

class SiteManager(models.Manager):
    """
    A simple manager for maintaining the current site separately from other sites.
    """
    def get_query_set(self, *args, **kwargs):
        return super(SiteManager, self).get_query_set(*args, **kwargs).filter(site=settings.SITE_ID)

class PostManager(SiteManager):
    
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
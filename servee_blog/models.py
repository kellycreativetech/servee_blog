# -*- coding: utf8 -*-
from datetime import datetime

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from django.contrib.sites.models import Site

if "taggit" in settings.INSTALLED_APPS:
    from taggit.managers import TaggableManager
else:
    def TaggableManager():
        return None

from servee_blog.managers import PostManager, SiteManager


def ig(L, i):
    for x in L:
        yield x[i]

class Section(models.Model):
    slug = models.SlugField(max_length=32, unique=True)
    name = models.CharField(max_length=32)
    content = models.TextField(blank=True, null=True)
    site = models.ForeignKey(Site, blank=True, null=True)
    
    def __unicode__(self):
        return u"%s" % self.name
    
    def save(self, *args, **kwargs):
        self.site = Site.objects.get_current()
        super(Section, self).save(*args, **kwargs)
    
    objects = SiteManager()
    
    class Meta:
        ordering = ["name",]
        # all of these reference the old table names.
        db_table = "biblion_section"


class Post(models.Model):
    
    sections = models.ManyToManyField(Section, related_name="posts", blank=True)
    site = models.ForeignKey(Site, blank=True, null=True)
    
    title = models.CharField(max_length=90)
    slug = models.SlugField()
    author = models.ForeignKey(User, related_name="posts")
    
    teaser_html = models.TextField()
    content_html = models.TextField()
    
    created = models.DateTimeField(default=datetime.now, editable=False) # when first revision was created
    updated = models.DateTimeField(null=True, blank=True, editable=False) # when last revision was create (even if not published)
    published = models.DateTimeField(null=True, blank=True) # original publish datetime
    
    tags = TaggableManager()
    
    @staticmethod
    def section_idx(slug):
        """
        given a slug return the index for it, pratically only for backwards compatability
        """
        try:
            return Section.objects.get(slug=slug).pk
        except Section.DoesNotExist:
            return None
    
    @property
    def section_slug(self):
        """
        For Backwards compatability
        """
        return self.section.slug
    
    def rev(self, rev_id):
        return self.revisions.get(pk=rev_id)
    
    def current(self):
        "the currently visible (latest published) revision"
        return self.revisions.exclude(published=None).order_by("-published")[0]
    
    def latest(self):
        "the latest modified (even if not published) revision"
        try:
            return self.revisions.order_by("-updated")[0]
        except IndexError:
            return None
    
    class Meta:
        ordering = ("-published",)
        get_latest_by = "published"
        # all of these reference the old table names.
        db_table = "biblion_post"
        
    
    objects = PostManager()
    
    def __unicode__(self):
        return self.title
    
    def save(self, **kwargs):
        self.updated_at = datetime.now()
        if not self.site:
            self.site = Site.objects.get_current()
        self.site = Site.objects.get_current()
        super(Post, self).save(**kwargs)
    
    def get_absolute_url(self):
        if self.published:
            name = "blog_post"
            kwargs = {
                "year": self.published.strftime("%Y"),
                "month": self.published.strftime("%m"),
                "day": self.published.strftime("%d"),
                "slug": self.slug,
            }
        else:
            name = "blog_post_pk"
            kwargs = {
                "post_pk": self.pk,
            }
        return reverse(name, kwargs=kwargs)


class Image(models.Model):
    
    post = models.ForeignKey(Post, related_name="images")
    
    image_path = models.ImageField(upload_to="images/%Y/%m/%d")
    url = models.CharField(max_length=150, blank=True)
    timestamp = models.DateTimeField(default=datetime.now, editable=False)
    
    site = models.ForeignKey(Site, blank=True, null=True)
    
    objects = SiteManager()
    
    class Meta:
        ordering = ("image_path",)
        # all of these reference the old table names.
        db_table = "biblion_image"
    
    def __unicode__(self):
        if self.pk is not None:
            return "{{ %d }}" % self.pk
        else:
            return "deleted image"

    def save(self, *args, **kwargs):
        self.site = Site.objects.get_current()
        super(Image, self).save(*args, **kwargs)

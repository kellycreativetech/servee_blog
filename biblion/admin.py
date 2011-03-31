from django.contrib import admin
from django.conf import settings
from django.utils.functional import curry

from biblion.models import Post, Image, Section
from biblion.forms import AdminPostForm
from biblion.utils import can_tweet


class ImageInline(admin.TabularInline):
    model = Image
    fields = ["image_path"]

class SectionAdmin(admin.ModelAdmin):
    list_display = ["name",]
    fields = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}

class PostAdmin(admin.ModelAdmin):  
    list_display = ["title", "published_flag",]
    list_filter = ["sections",]
    form = AdminPostForm
    fields = [
        "title",
        "slug",
        "author",
        "teaser",
        "content",
        "publish",
        "sections",
    ]
    if can_tweet():
        fields.append("tweet")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        ImageInline,
    ]
    
    def __init__(self, *args, **kwargs):
        if "taggit" in settings.INSTALLED_APPS:
            self.fields.append("tags")
        super(PostAdmin, self).__init__(*args, **kwargs)
    
    def published_flag(self, obj):
        return bool(obj.published)
    published_flag.short_description = "Published"
    published_flag.boolean = True
    
    def save_form(self, request, form, change):
        # this is done for explicitness that we want form.save to commit
        # form.save doesn't take a commit kwarg for this reason
        return form.save()


admin.site.register(Post, PostAdmin)
admin.site.register(Image)
admin.site.register(Section, SectionAdmin)

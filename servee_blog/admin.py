from django.contrib import admin
from django.conf import settings

from servee_blog.models import Post, Image, Section


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
    fields = [
        "title",
        "slug",
        "author",
        "teaser_html",
        "content_html",
        "published",
        "sections",
    ]
    exclude = [
        "site",
    ]
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


admin.site.register(Post, PostAdmin)
admin.site.register(Image)
admin.site.register(Section, SectionAdmin)

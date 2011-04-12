from servee import frontendadmin
from servee_blog.models import Post, Section
from servee_blog.admin import PostAdmin as StdPostAdmin, SectionAdmin as StdSectionAdmin


class PostAdmin(frontendadmin.ServeeModelAdmin, StdPostAdmin):
    excludes = ["author",]
    
    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        
        super(PostAdmin, self).save_model(request, obj, form, change)

frontendadmin.site.register(Post, PostAdmin)


class SectionAdmin(frontendadmin.ServeeModelAdmin, StdSectionAdmin):
    pass

frontendadmin.site.register(Section, SectionAdmin)

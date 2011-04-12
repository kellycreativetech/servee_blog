from django.conf.urls.defaults import *

from django.views.generic.simple import direct_to_template


urlpatterns = patterns("",
    url(r"^$", "servee_blog.views.blog_index", name="blog"),
    url(r"^feeds/", "servee_blog.views.blog_feed", name="blog_feed_all"),
    url(r"^feeds/(?P<section>[\w\-]+)/", "servee_blog.views.blog_feed", name="blog_feed"),
    url(r"^archive/$", "servee_blog.views.blog_index", kwargs={"template":"servee_blog/archive.html"}, name="blog_archive"),
    url(r"^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$", "servee_blog.views.blog_post_detail", name="blog_post"),
    url(r"^post/(?P<post_pk>\d+)/$", "servee_blog.views.blog_post_detail", name="blog_post_pk"),
    url(r"^(?P<section>[-\w]+)/$", "servee_blog.views.blog_section_list", name="blog_section"),
    url(r"^(?P<section>[-\w]+)/archive/$", "servee_blog.views.blog_section_list", kwargs={"template":"servee_blog/archive.html"}, name="blog_section_archive"),
)
from django.conf.urls.defaults import *

from django.views.generic.simple import direct_to_template


urlpatterns = patterns("",
    url(r"^$", "biblion.views.blog_index", name="blog"),
    url(r"^archive/$", "biblion.views.blog_index", kwargs={"template":"biblion/archive.html"}, name="blog_archive"),
    url(r"^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$", "biblion.views.blog_post_detail", name="blog_post"),
    url(r"^post/(?P<post_pk>\d+)/$", "biblion.views.blog_post_detail", name="blog_post_pk"),
    url(r"^(?P<section>[-\w]+)/$", "biblion.views.blog_section_list", name="blog_section"),
    url(r"^(?P<section>[-\w]+)/archive/$", "biblion.views.blog_section_list", kwargs={"template":"biblion/archive.html"}, name="blog_section_archive"),
)
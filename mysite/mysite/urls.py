from django.conf.urls import patterns, include, url
from django.contrib import admin
from shopcart.views import RegisterCreditcardView

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('shopcart.urls')),
    url(r'^cart/$', RegisterCreditcardView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
]
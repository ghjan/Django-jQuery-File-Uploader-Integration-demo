from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangoUpload.views.home', name='home'),
    # url(r'^djangoUpload/', include('djangoUpload.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', admin.site.urls),

    # For the Django Jquery Upload
    url(r'^upload/', include('upload.urls')),
    # (r'^upload/', 'upload.views.Upload')),

    # (r'^studyview/', include('studyview.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

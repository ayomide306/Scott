from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("post.urls", namespace="post")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("", include("account.urls", namespace="account")),
    path("", include("dashboard.urls", namespace="dashboard")),
    path("", include("newsletter.urls", namespace="newsletter")),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


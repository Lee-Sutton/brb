from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from brb.users.views_integration import IntegrationView

urlpatterns = [
    path('ht/', include('health_check.urls')),
    path("", TemplateView.as_view(template_name="pages/home.html"),
         name="home"),
    path("about/", TemplateView.as_view(template_name="pages/about.html"),
         name="about",
         ),

    path('integration/', IntegrationView.as_view()),

    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path(
        "users/",
        include("brb.users.urls", namespace="users"),
    ),
    path("accounts/", include("allauth.urls")),

    # rest authentication
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    # terminal logs
    path(
        'terminal_logs/',
        include('brb.terminal_logs.urls', namespace="terminal_logs"),
    ),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/",
                            include(debug_toolbar.urls))] + urlpatterns

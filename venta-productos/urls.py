from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.views.generic.base import RedirectView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import PasswordResetConfirmView, PasswordResetView

schema_view = get_schema_view(
    openapi.Info(
        title="venta-productos API",
        default_version="v1",
        description="Sistema de ventas de productos a clientes",
    ),
    public=False,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("users/", include("users.urls")),
    path("reset-password/", PasswordResetView.as_view()),
    path(
        "reset-password/<str:uidb64>/<str:token>/", PasswordResetConfirmView.as_view()
    ),
    path("", include("core.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path(
            "",
            RedirectView.as_view(pattern_name="schema-swagger-ui"),
            name="go-to-docs",
        )
    ]

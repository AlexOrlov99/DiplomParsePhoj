from django.contrib import admin
from django.conf import settings
from django.urls import (
    path,
    include,
)
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from apps.auths.views import CustomUserViewSet
from apps.rezume.views import (
    ResumeViewSet,
    )

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path(settings.ADMIN_SITE_URL, admin.site.urls),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)


if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

# ------------------------------------------------
# API-Endpoints

router: DefaultRouter = DefaultRouter()
  
router.register('auths', CustomUserViewSet)
router.register('resume', ResumeViewSet)

urlpatterns += [
    path('api/v1/', include(router.urls)),
    path(
        'api/v1/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'api/v1/token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
    ),
]
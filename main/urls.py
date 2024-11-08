from rest_framework.routers import DefaultRouter
from main import views

router = DefaultRouter()
router.register(r'userprofiles', views.UserProfileViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # другие URL-адреса
]

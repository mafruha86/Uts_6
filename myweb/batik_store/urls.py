from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KategoriViewSet, ProdukViewSet, StokViewSet

router = DefaultRouter()
router.register(r'kategori', KategoriViewSet)
router.register(r'produk', ProdukViewSet)
router.register(r'stok', StokViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

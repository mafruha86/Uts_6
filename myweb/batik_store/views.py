from rest_framework import viewsets
from .models import Kategori, Produk, Stok
from .serializers import KategoriSerializer, ProdukSerializer, StokSerializer

class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

class StokViewSet(viewsets.ModelViewSet):
    queryset = Stok.objects.all()
    serializer_class = StokSerializer

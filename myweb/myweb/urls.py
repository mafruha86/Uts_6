from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('batik_store/', include('batik_store.urls')),  # Ganti 'strobatik' dengan nama aplikasi Anda
    # path('nama_aplikasi/', include('nama_aplikasi.urls')),  # Contoh untuk menambahkan aplikasi lain
]

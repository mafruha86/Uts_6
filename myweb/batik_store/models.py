from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Produk(models.Model):
    nama = models.CharField(max_length=200)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama

class Stok(models.Model):
    produk = models.OneToOneField(Produk, on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Stok {self.produk.nama}: {self.jumlah} pcs"

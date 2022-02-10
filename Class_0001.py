class Soru():

    def __init__(self, dogruSayisi, yanlisSayisi):
        self.dogruSayisi = dogruSayisi
        self.yanlisSayisi = yanlisSayisi

    def netSayisi(self):
        silinenDogruCevap = self.yanlisSayisi / 4
        netSayisi = self.dogruSayisi - silinenDogruCevap
        return netSayisi

    def hesapla(self, netsayisi):
        return netsayisi*2

class Ogrenci():
    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinifi):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinifi = ogrenciSinifi

ogrenciAdi = input("Lütfen Öğrenci Adını giriniz :")
ogrencisoyadi = input("Lütfen Öğrenci Soyadını giriniz :")
ogrenciSinifi = input("Lütfen Öğrenci Sınıfını giriniz :")

ogr = Ogrenci(ogrenciAdi, ogrencisoyadi, ogrenciSinifi)

dogruCevap = int(input("Lütfen Doğru Cevap sayısını giriniz : "))
yanlisCevap = int(input("Lütfen yanlış cevap sayısını giriniz :"))

soru = Soru(dogruCevap, yanlisCevap)

netSayisi = soru.netSayisi()
puan = soru.hesapla(netSayisi)

print("Adı : {}, Soyadı :  {}, Sınıfı : {}, Puanı : {} " .format(
            ogr.ogrenciAdi,
            ogr.ogrenciSoyadi,
            ogr.ogrenciSinifi,
            puan)
)



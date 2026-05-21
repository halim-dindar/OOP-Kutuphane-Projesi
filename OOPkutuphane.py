from abc import ABC, abstractmethod


# ---------------- KAYNAK ----------------

class Kaynak(ABC):

    def __init__(self, baslik, kayitNo):
        self._baslik = baslik
        self._kayitNo = kayitNo

    @property
    def baslik(self):
        return self._baslik

    @baslik.setter
    def baslik(self, value):
        self._baslik = value

    @property
    def kayitNo(self):
        return self._kayitNo

    @kayitNo.setter
    def kayitNo(self, value):
        self._kayitNo = value


# ---------------- KITAP ----------------

class Kitap(Kaynak):

    def __init__(self, baslik, kayitNo, yazar, sayfa_sayisi):
        super().__init__(baslik, kayitNo)

        self._yazar = yazar
        self._sayfa_sayisi = sayfa_sayisi

    @property
    def yazar(self):
        return self._yazar

    @yazar.setter
    def yazar(self, value):
        self._yazar = value

    @property
    def sayfa_sayisi(self):
        return self._sayfa_sayisi

    @sayfa_sayisi.setter
    def sayfa_sayisi(self, value):
        self._sayfa_sayisi = value

    def __str__(self):
        return f"{self.baslik} | {self.kayitNo} | {self.yazar} | {self.sayfa_sayisi} sayfa"


# ---------------- DERGI ----------------

class Dergi(Kaynak):

    def __init__(self, baslik, kayitNo, yayin_donemi, sayi_no):
        super().__init__(baslik, kayitNo)

        self._yayin_donemi = yayin_donemi
        self._sayi_no = sayi_no

    @property
    def yayin_donemi(self):
        return self._yayin_donemi

    @yayin_donemi.setter
    def yayin_donemi(self, value):
        self._yayin_donemi = value

    @property
    def sayi_no(self):
        return self._sayi_no

    @sayi_no.setter
    def sayi_no(self, value):
        self._sayi_no = value

    def __str__(self):
        return f"{self.baslik} | {self.kayitNo} | {self.yayin_donemi} | Sayı:{self.sayi_no}"


# ---------------- SOYUT ISLEM ----------------

class Islem(ABC):

    @abstractmethod
    def ekle(self):
        pass

    @abstractmethod
    def sil(self):
        pass

    @abstractmethod
    def guncelle(self):
        pass

    @abstractmethod
    def listele(self):
        pass


# ---------------- KITAP ISLEM ----------------

class KitapIslem(Islem):

    def __init__(self):
        self.kitaplar = []

    def ekle(self):

        kayitNo = input("Kayıt No: ")

        for kitap in self.kitaplar:
            if kitap.kayitNo == kayitNo:
                print("Bu kayıt numarası kullanılıyor.")
                return

        baslik = input("Kitap Adı: ")
        yazar = input("Yazar: ")
        sayfa = int(input("Sayfa Sayısı: "))

        yeni = Kitap(
            baslik,
            kayitNo,
            yazar,
            sayfa
        )

        self.kitaplar.append(yeni)

        print("Kitap eklendi.")
        print("Toplam Kitap Sayısı:", len(self.kitaplar))

    def sil(self):

        kayitNo = input("Silinecek kayıt no: ")

        for kitap in self.kitaplar:
            if kitap.kayitNo == kayitNo:
                self.kitaplar.remove(kitap)

                print("Kitap silindi.")
                return

        print("Kayıt bulunamadı")

    def guncelle(self):

        kayitNo = input("Güncellenecek kayıt no: ")

        for kitap in self.kitaplar:

            if kitap.kayitNo == kayitNo:

                kitap.baslik = input("Yeni Başlık: ")
                kitap.yazar = input("Yeni Yazar: ")
                kitap.sayfa_sayisi = int(
                    input("Yeni Sayfa Sayısı: ")
                )

                print("Kitap güncellendi")
                return

        print("Kayıt bulunamadı")

    def listele(self):

        if len(self.kitaplar) == 0:
            print("Kayıt bulunamadı")
            return

        for kitap in self.kitaplar:
            print(kitap)


# ---------------- DERGI ISLEM ----------------

class DergiIslem(Islem):

    def __init__(self):
        self.dergiler = []

    def ekle(self):

        kayitNo = input("Kayıt No: ")

        for dergi in self.dergiler:
            if dergi.kayitNo == kayitNo:
                print("Bu kayıt numarası kullanılıyor.")
                return

        baslik = input("Dergi Adı: ")
        yayin = input("Yayın Dönemi: ")
        sayi = input("Sayı No: ")

        yeni = Dergi(
            baslik,
            kayitNo,
            yayin,
            sayi
        )

        self.dergiler.append(yeni)

        print("Dergi eklendi.")
        print("Toplam Dergi Sayısı:", len(self.dergiler))

    def sil(self):

        kayitNo = input("Silinecek kayıt no: ")

        for dergi in self.dergiler:
            if dergi.kayitNo == kayitNo:
                self.dergiler.remove(dergi)

                print("Dergi silindi.")
                return

        print("Kayıt bulunamadı")

    def guncelle(self):

        kayitNo = input("Güncellenecek kayıt no: ")

        for dergi in self.dergiler:

            if dergi.kayitNo == kayitNo:

                dergi.baslik = input("Yeni Başlık: ")
                dergi.yayin_donemi = input(
                    "Yeni Yayın Dönemi: "
                )

                print("Dergi güncellendi")
                return

        print("Kayıt bulunamadı")

    def listele(self):

        if len(self.dergiler) == 0:
            print("Kayıt bulunamadı")
            return

        for dergi in self.dergiler:
            print(dergi)


# ---------------- MENU ----------------

kitapIslem = KitapIslem()
dergiIslem = DergiIslem()

while True:

    print("\n----- KÜTÜPHANE YÖNETİM SİSTEMİ -----")

    print("1. Kitap Ekle")
    print("2. Kitap Sil")
    print("3. Kitap Güncelle")
    print("4. Kitapları Listele")
    print("5. Dergi Ekle")
    print("6. Dergi Sil")
    print("7. Dergi Güncelle")
    print("8. Dergileri Listele")
    print("9. Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        kitapIslem.ekle()

    elif secim == "2":
        kitapIslem.sil()

    elif secim == "3":
        kitapIslem.guncelle()

    elif secim == "4":
        kitapIslem.listele()

    elif secim == "5":
        dergiIslem.ekle()

    elif secim == "6":
        dergiIslem.sil()

    elif secim == "7":
        dergiIslem.guncelle()

    elif secim == "8":
        dergiIslem.listele()

    elif secim == "9":
        print("Program kapatılıyor...")
        break

    else:
        print("Hatalı seçim")
import random
import time

class Kumanda():
    def __init__(self, tv_durum="kapalı", tv_ses=0, kanal_listesi=None, kanal="TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.min_ses = 0
        self.max_ses = 32
        
        # Başlangıçta boş liste kontrolü
        if kanal_listesi is None:
            self.kanal_listesi = ["TRT", "Kanal D", "Show TV", "ATV"]
        else:
            self.kanal_listesi = kanal_listesi
            
        # Başlangıç kanalının listede olduğundan emin ol
        if kanal in self.kanal_listesi:
            self.kanal = kanal
        elif self.kanal_listesi: # Liste boş değilse ilk kanalı ata
            self.kanal = self.kanal_listesi[0]
        else: # Liste boşsa
            self.kanal = "Kanal Yok"

    def _tv_kapali_mi(self):
        """Yardımcı metot: TV kapalıysa uyarı verir ve True döner."""
        if self.tv_durum == "kapalı":
            print("TV şu an kapalı. Lütfen önce televizyonu açın.")
            return True
        return False

    def tv_ac(self):
        if self.tv_durum == "açık":
            print("Televizyon zaten açık.")
        else:
            print("Televizyon açılıyor...")
            time.sleep(0.5)
            self.tv_durum = "açık"
            print("Televizyon açıldı.")

    def tv_kapat(self):
        if self.tv_durum == "kapalı":
            print("Televizyon zaten kapalı.")
        else:
            print("Televizyon kapanıyor...")
            time.sleep(0.5)
            self.tv_durum = "kapalı"
            print("Televizyon kapandı.")

    def ses_artir(self):
        if self._tv_kapali_mi():
            return

        if self.tv_ses < self.max_ses:
            self.tv_ses += 1
            print("Ses:", self.tv_ses)
        else:
            print(f"Ses maksimum seviyede ({self.max_ses}).")

    def ses_azalt(self):
        if self._tv_kapali_mi():
            return

        if self.tv_ses > self.min_ses:
            self.tv_ses -= 1
            print("Ses:", self.tv_ses)
        else:
            print(f"Ses minimum seviyede ({self.min_ses}).")

    def kanal_ekle(self, kanal_ismi):
        # TV kapalıyken de kanal eklenebilir, bu bir tercih.
        # Eğer kapalıyken eklenemesin istersen:
        # if self._tv_kapali_mi():
        #     return
        
        if kanal_ismi not in self.kanal_listesi:
            print(f"'{kanal_ismi}' kanalı ekleniyor...")
            time.sleep(1)
            self.kanal_listesi.append(kanal_ismi)
            print("Kanal eklendi.")
            # Eğer hiç kanal yoksa, eklenen ilk kanalı aktif kanal yap
            if self.kanal == "Kanal Yok":
                self.kanal = kanal_ismi
        else:
            print(f"'{kanal_ismi}' kanalı listede zaten mevcut.")


    def kanal_silme(self, silinecek_kanal):
        # if self._tv_kapali_mi(): # TV kapalıyken de silinebilir
        #     return
            
        if silinecek_kanal in self.kanal_listesi:
            print(f"'{silinecek_kanal}' kanalı siliniyor...")
            self.kanal_listesi.remove(silinecek_kanal)
            print("Kanal silindi.")

            # Eğer silinen kanal aktif kanalsa senkronizasyon yap
            if silinecek_kanal == self.kanal:
                if self.kanal_listesi: # Liste boş kalmadıysa
                    self.kanal = self.kanal_listesi[0]
                    print(f"Aktif kanal silindi. İlk kanala geçildi: {self.kanal}")
                else: # Liste boş kaldıysa
                    self.kanal = "Kanal Yok"
                    print("Son kanal da silindi. Listede hiç kanal kalmadı.")
        else:
            print(f"'{silinecek_kanal}' adında bir kanal bulunamadı.")

    def rastgele_kanal(self):
        if self._tv_kapali_mi():
            return

        if not self.kanal_listesi:
            print("Kanal listesi boş. Rastgele kanala geçilemiyor.")
            return

        # O anki kanaldan farklı bir kanala geç
        if len(self.kanal_listesi) == 1:
            print("Listede sadece bir kanal var, rastgele geçiş yapılamıyor.")
            return
            
        yeni_kanal = self.kanal
        while yeni_kanal == self.kanal:
            yeni_kanal = random.choice(self.kanal_listesi)
            
        self.kanal = yeni_kanal
        print(f"Şu anki kanal: {self.kanal}")

    def _kanal_degistir(self, yön):
        """Yardımcı metot: Sonraki/Önceki kanal için ortak mantık"""
        if self._tv_kapali_mi():
            return

        if not self.kanal_listesi:
            print("Kanal listesi boş. Kanal değiştirilemiyor.")
            return
        
        if self.kanal not in self.kanal_listesi:
             # Eğer aktif kanal (örn: "Kanal Yok") listede değilse, ilk kanaldan başla
            self.kanal = self.kanal_listesi[0]
        else:
            mevcut_index = self.kanal_listesi.index(self.kanal)
            liste_uzunlugu = len(self.kanal_listesi)
            
            # Modulo aritmetiği ile liste sonundan başına (veya tersi) dönme
            yeni_index = (mevcut_index + yön + liste_uzunlugu) % liste_uzunlugu
            self.kanal = self.kanal_listesi[yeni_index]
        
        print(f"Kanal: {self.kanal}")

    def sonraki_kanal(self):
        self._kanal_degistir(yön=1)

    def onceki_kanal(self):
        self._kanal_degistir(yön=-1)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return (f"--- Televizyon Bilgileri ---\n"
                f"TV Durumu: {self.tv_durum}\n"
                f"TV Ses: {self.tv_ses}\n"
                f"Aktif Kanal: {self.kanal}\n"
                f"Kanal Listesi ({len(self)} adet): {', '.join(self.kanal_listesi)}\n"
                f"-----------------------------")

# --- ANA UYGULAMA DÖNGÜSÜ ---

kumanda1 = Kumanda()

while True:
    print("""
📺 Televizyon Uygulaması 📺
      
1.  TV Aç
2.  TV Kapat
3.  Ses Artır   (+)
4.  Ses Azalt   (-)
5.  Sonraki Kanal (>>)
6.  Önceki Kanal  (<<)
7.  Rastgele Kanala Geç
8.  Kanal Ekle
9.  Kanal Sil
10. Kanal Sayısı Öğren
11. Televizyon Bilgileri (Tüm Liste)

Çıkmak için 'q' ya basın.
""")

    işlem = input("İşlemi seçiniz (1-11): ").strip() # strip() ile boşlukları temizle

    if işlem == "q":
        print("Program sonlandırılıyor...")
        kumanda1.tv_kapat() # Kapatarak çıkmak daha mantıklı
        break
        
    elif işlem == "1":
        kumanda1.tv_ac()
        
    elif işlem == "2":
        kumanda1.tv_kapat()
        
    elif işlem == "3":
        kumanda1.ses_artir()
        
    elif işlem == "4":
        kumanda1.ses_azalt()

    elif işlem == "5":
        kumanda1.sonraki_kanal()

    elif işlem == "6":
        kumanda1.onceki_kanal()

    elif işlem == "7":
        kumanda1.rastgele_kanal()
        
    elif işlem == "8":
        kanal_isimleri = input("Eklenecek kanal isimlerini ',' (virgül) ile ayırarak girin: ")
        kanal_listesi = [isim.strip() for isim in kanal_isimleri.split(",") if isim.strip()]
        
        if not kanal_listesi:
            print("Geçerli bir kanal ismi girmediniz.")
        else:
            for eklenecek_kanal in kanal_listesi:
                kumanda1.kanal_ekle(eklenecek_kanal)
                
    elif işlem == "9":
        print("Mevcut Kanallar:", ", ".join(kumanda1.kanal_listesi))
        silinecek_kanal = input("Silinecek kanalın adını tam olarak yazın: ").strip()
        if silinecek_kanal:
            kumanda1.kanal_silme(silinecek_kanal)
        else:
            print("Geçerli bir isim girmediniz.")

    elif işlem == "10":
        print("Toplam Kanal Sayısı:", len(kumanda1))
        
    elif işlem == "11":
        print(kumanda1) # __str__ metodu sayesinde
        
    else:
        print("Geçersiz işlem. Lütfen 1-11 arasında bir sayı veya 'q' girin.")
    
    # Her işlemden sonra kısa bir bekleme
    if işlem != "q":
        time.sleep(1)
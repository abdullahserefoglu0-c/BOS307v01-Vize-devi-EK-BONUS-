
#KODLAMA EGZERSİZİ - KUMANDA SINIFI GELİŞTİRME : 

import random
import time

class kumanda():
    def __init__(self,tv_durum = "kapalı",tv_ses=0,kanal_listesi=["trt"],kanal ="trt"):
       self.tv_durum = tv_durum
       self.tv_ses = tv_ses
       self.kanal_listesi = kanal_listesi
       self.kanal = kanal
    def tv_ac(self):
        if self.tv_durum=="açık":
            print("televizyon zaten açık...")
        else:
            print("televizyon açılıyor...")
            self.tv_durum = "açık"
    def tv_kapat(self):
        if self.tv_durum=="kapalı":
            print("televizyon zaten kapalı")
        else:
            print("televizyon kapanıyor...")
            self.tv_durum = "kapalı"
    def ses_ayarları(self):
        while True:
            cevap = input("sesi azalt: '<'\nsesi artır: '>'\nçıkış: çıkış")
            if cevap=="<":
                if self.tv_ses!=0:
                    self.tv_ses-=1
                    print("ses:",self.tv_ses)
            elif cevap ==">":
                if self.tv_ses!=31:
                    self.tv_ses+=1
                    print("ses:",self.tv_ses)
            else:
                print("ses güncellendi:",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):

        print("kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("kanal eklendi...")

    def rastgele_kanal(self):

        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele] 
        print("şu naki kanal:",self.kanal)

    def __len__(self):
        
        return len(self.kanal_listesi)
    
    def __str__(self):
        return "tv durumu: {}\ntv ses: {}\nkanal listesi: {}\nşu anki kanal {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)
    

    def kanal_silme(self): # ben ekledim bunu
        print(self.kanal_listesi)
        silincek_kanal = input("silinecek kanalı yazın:")
        if silincek_kanal in self.kanal_listesi:
            self.kanal_listesi.remove(silincek_kanal)  # Listeden eleman silmek için remove() metodu kullanılmalı.
            print("yeni kanal listesi:",self.kanal_listesi)
        else:
            print("kanal bulunamadı...")
    

kumanda1=kumanda()    
print("""
televizyon uygulaması 
    
      1.tv aç
      2.tv kapat
      3.ses ayarları
      4.kanal ekle
      5.kanal sayısı öğrenme
      6.rastgele kanala geçme
      7.televizyon bilgileri
      8.kanal sil
      çıkmak için 'q' ya basın 
""") 

while True:
    işlem = input("işlemi seçiniz:")
    if işlem == "q":
        print("program sonlandırılıyor...")
        break
    elif işlem=="1":
        kumanda1.tv_ac()
    elif işlem=="2":
        kumanda1.tv_kapat()
    elif işlem == "3":
        kumanda1.ses_ayarları()
    elif işlem== "4":
        kanal_isimleri=input("kanal isimlerini ',' ile ayırarak girin:")
        kanal_listesi = kanal_isimleri.split(",")   # .split(",") = virgül gördüğü yerde metni böler ve her parçayı bir liste elemanı yapar.
        for eklenecekler in kanal_listesi:
            kumanda1.kanal_ekle(eklenecekler)
    elif işlem=="5":
        print("kanal sayısı:",len(kumanda1))
    elif işlem== "6":
        kumanda1.rastgele_kanal()
    elif işlem == "7":
        print(kumanda1)
    elif işlem=="8":
        kumanda1.kanal_silme()
    else:
        print("geçersiz işlem")




#!/usr/bin/env python3
# Abartılı Yavaş Hesap Makinesi
# Bu kod gerçekten çalışır. Sabırlı olun.
# Gizli not: Bazen en yavaş yollar en doğru yollardır, acele etmek bazen yanlış kararları getirir.

import time
import sys

def yavas_hesapla(islem):
    print("Hesaplama başladı...")
    print("Lütfen bekleyin, evrenin en yavaş hesap makinesi çalışıyor.")
    time.sleep(5)  # Gerçekten yavaş
    print("Hala düşünüyorum...")
    time.sleep(3)
    try:
        sonuc = eval(islem)
        print(f"Sonuç bulundu: {sonuc}")
        print("Bu sonuca ulaşmak için tam {8} saniye harcadık. Tebrikler!")
        return sonuc
    except Exception as e:
        print(f"Hata: {e}. Ama yavaş yavaş çözeceğiz.")
        return None

if __name__ == "__main__":
    print("=== Abartılı Yavaş Hesap Makinesi v1.0 ===")
    print("Örnek: 2+2 veya 10*5")
    islem = input("İşlemi girin: ")
    yavas_hesapla(islem)
    print("\nTeşekkürler. Bir dahaki sefere daha yavaş olacağız.")

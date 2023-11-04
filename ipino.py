import subprocess
import sys

# Gereken kütüphane listesi
REQUIRED_LIBRARIES = ["requests", "colorama"]

# Eksik kütüphaneleri kontrol et ve kur
def eksik_kutuphaneli_kur():
    eksik_kutuphaneler = []
    for lib in REQUIRED_LIBRARIES:
        try:
            __import__(lib)
        except ImportError:
            eksik_kutuphaneler.append(lib)

    if eksik_kutuphaneler:
        print(f"Eksik kütüphaneler kuruluyor: {', '.join(eksik_kutuphaneler)}")
        for lib in eksik_kutuphaneler:
            subprocess.call([sys.executable, "-m", "pip", "install", lib])

# Devam etmeden önce eksik kütüphaneleri kur
eksik_kutuphaneli_kur()


import sys
import requests
from colorama import Fore, Style, init
import socket

# Colorama'yi baslat
init(autoreset=True)

# Banner
banner = f'''{Fore.LIGHTWHITE_EX}
            ▄  ▄ ▀█▄
  ▄████████▄██▄██▄██
  █████████████▄████▌
  ▌████████████▀▀▀▀▀
 ▀ ▐█▄▐█▄▐█▄▐█▄{Style.RESET_ALL}
'''

print(banner)

def bilgi_yaz(anahtar, deger):
    if deger:
        print(f"{Fore.GREEN}{anahtar}:{Style.RESET_ALL} {deger}")

def ip_bilgisi_al(ip_adresi):
    try:
        # Ücretsiz "ipinfo.io" API'sini kullanarak IP bilgisi alın
        yanıt = requests.get(f"https://ipinfo.io/{ip_adresi}/json")
        veri = yanıt.json()

        # Var ise ilgili bilgileri renkli olarak yazdır
        bilgi_yaz("IP Adresi", veri.get("ip"))
        bilgi_yaz("Ana Makine Adı", veri.get("hostname"))
        bilgi_yaz("Şehir", veri.get("city"))
        bilgi_yaz("Bölge", veri.get("region"))
        bilgi_yaz("Ülke", veri.get("country"))
        bilgi_yaz("Konum (Enlem, Boylam)", veri.get("loc"))
        bilgi_yaz("Google Haritalar Konumu", f"https://maps.google.com/?q={veri.get('loc')}")
        bilgi_yaz("Organizasyon", veri.get("org"))
        bilgi_yaz("Zaman Dilimi", veri.get("timezone"))
        bilgi_yaz("Posta Kodu", veri.get("postal"))
        bilgi_yaz("ASN (Otonom Sistem Numarası)", veri.get("asn"))
        bilgi_yaz("Ağ Aralığı", veri.get("network"))
        bilgi_yaz("CIDR", veri.get("cidr"))
        bilgi_yaz("Suistimal İletişim Bilgisi", veri.get("abuse"))
    except Exception as e:
        print(f"{Fore.RED}Bir hata oluştu:{Style.RESET_ALL} {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.LIGHTYELLOW_EX}Kullanım:{Style.RESET_ALL} ipino.py <IP veya Alan Adı>")
        sys.exit(1)
    
    hedef = sys.argv[1]

    try:
        # Girdinin bir IP adresi olup olmadığını kontrol edin
        ip_adresi = socket.gethostbyname(hedef)
        ip_bilgisi_al(ip_adresi)
    except socket.gaierror:
        # Eğer girdi bir IP adresi değilse, alan adı olarak kabul edin
        ip_bilgisi_al(hedef)
import subprocess
import sys

REQUIRED_LIBRARIES = ["requests", "colorama"]

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

eksik_kutuphaneli_kur()

import sys
import requests
import re
import argparse
from colorama import init, Fore, Back, Style

BANNER = """
        ───▄▄▄
        ─▄▀░▄░▀▄
        ─█░█▄▀░█
        ─█░▀▄▄▀█▄█▄▀
        ▄▄█▄▄▄▄███▀
"""

def main():
    init(autoreset=True)

    print(Fore.LIGHTRED_EX + BANNER + Fore.LIGHTBLUE_EX + "                      by AtaReis\n")

    parser = argparse.ArgumentParser(
        usage="gary.py URL [-o OUTPUT] [-p PROXY]"
    )
    parser.add_argument("url", help="İşlem yapılacak URL")
    parser.add_argument("-o", "--output", help="Çıktı dosyasının adı")
    parser.add_argument("-p", "--proxy", help="SOCKS5 proxy adresi (örn. 127.0.0.1:1080)")
    args = parser.parse_args()

    url = args.url
    
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    html_content = get_html_content(url, args.proxy)

    if html_content:
        urls = extract_urls(html_content)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as output_file:
                for url in urls:
                    output_file.write(url + "\n")
            print(Fore.LIGHTGREEN_EX + f"+İçerikler başarıyla {args.output} dosyasına kaydedildi.")
        else:
            for url in urls:
                print(Fore.LIGHTWHITE_EX + url)
    else:
        print(Fore.RED + "-URL'den içerik alınamadı.")

def get_html_content(url, proxy):
    proxies = None
    if proxy:
        proxies = {
            "http": f"socks5://{proxy}",
            "https": f"socks5://{proxy}"
        }

    try:
        response = requests.get(url, proxies=proxies)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(Fore.RED + "-Hata:", e)
        return None

def extract_urls(html_content):
    urls = re.findall(r"https?://\S+", html_content)
    return urls

if __name__ == "__main__":
    main()

import requests
import subprocess
import os

def uygulama_indir(url, dosya_adı):
    response = requests.get(url)
    with open(dosya_adı, 'wb') as dosya:
        dosya.write(response.content)

def uygulama_calistir(dosya_adı):
    try:
        subprocess.run([dosya_adı])
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    indirilen_dosya_adı = "dosyanın adı" // file name
    indirilecek_url = "uygulamayı indireceği siteyi yazın"  // where to download the file only url
    uygulama_indir(indirilecek_url, indirilen_dosya_adı)
    uygulama_calistir(indirilen_dosya_adı)
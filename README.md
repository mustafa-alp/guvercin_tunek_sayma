# Güvercin Yuvası Sayıcı

Bu proje, görüntü işleme kullanarak güvercin yuvalarını tespit eden ve sayan bir Python uygulamasıdır.

## Gereksinimler

- Python 3.6 veya üzeri
- pip (Python paket yöneticisi)
- Git

## Kurulum

1. Projeyi indirin:
```bash
git clone https://github.com/mustafa-alp/guvercin_tunek_sayma.git
cd guvercin_tunek_sayma
```

2. Sanal ortam oluşturun ve aktifleştirin:
```bash
# Windows için
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac için
python3 -m venv .venv
source .venv/bin/activate
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

## Kullanım

1. Programı çalıştırmak için:
```bash
python main.py
```

2. Veri seti oluşturmak için:
```bash
python veri_seti_olusturma.py
```

## Proje Yapısı

- `main.py`: Ana uygulama dosyası
- `veri_seti_olusturma.py`: Veri seti oluşturma aracı
- `Dataset/`: Eğitim veri seti
- `best.pt`: Eğitilmiş model
- `yeni_goruntuler/`: Test için kullanılacak görüntüler
- `veri/`: İşlenmiş veriler

## Notlar

- Model dosyası (`best.pt`) büyük olduğu için GitHub'a yüklenmemiştir. Modeli ayrıca indirmeniz gerekecektir.
- Veri seti dosyaları da GitHub'a yüklenmemiştir. Kendi veri setinizi oluşturmanız veya mevcut bir veri seti kullanmanız gerekecektir.

## Önemli Uyarı

Bu proje sadece indirme amaçlıdır. Lütfen projeyi fork etmeyin veya kendi GitHub reponuzda paylaşmayın. Tüm hakları saklıdır.

## Lisans

Bu proje özel lisans altında dağıtılmaktadır. İzinsiz kullanımı ve dağıtımı yasaktır. 
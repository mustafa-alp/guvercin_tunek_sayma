# Güvercin Yuvası Sayıcı

Bu proje, görüntü işleme kullanarak güvercin yuvalarını tespit eden ve sayan bir Python uygulamasıdır.

## Gereksinimler

- Python 3.6 veya üzeri
- pip (Python paket yöneticisi)
- Git

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/KULLANICI_ADINIZ/pigeon-roost-counter.git
cd pigeon-roost-counter
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

## Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: Açıklama'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Bir Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın. 
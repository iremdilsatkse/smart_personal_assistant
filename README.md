# Akıllı Kişisel Asistan

Akıllı asistan uygulaması, Gemini 2.0 Flash API'sini kullanarak notlarınızı ve etkinliklerinizi yönetmenizi sağlar. Not ekleyebilir, etkinlik ekleyebilir, not ve etkinlikleri görüntüleyebilir, özetleyebilir ve sohbet edebilirsiniz.

## Özellikler

- Not ekleme ve listeleme
- Etkinlik ekleme ve listeleme
- Not ve etkinlik özetleme (Gemini API ile)
- Akıllı sohbet
- SQLite veritabanı desteği

## Kurulum

1. Depoyu klonlayın veya dosyaları indirin.
2. Gerekli Python paketlerini yükleyin:
   ```sh
   pip install -r requirements.txt
   ```
3. .env dosyasına Gemini API anahtarınızı ekleyin:

## Kullanım

Terminalde aşağıdaki komutla uygulamayı başlatın:
```sh
python main.py
```

Terminalden gelen yanıtla birlikte bir komut girin.
```sh
Komutlar:

- Not Ekle
- Etkinlik Ekle
- Notları Göster
- Etkinlikleri Göster
- Sohbet Et
- Çıkış
```

## Dosya Yapısı

- [`main.py`](main.py): Ana uygulama dosyası
- [`assistant.py`](assistant.py): Gemini API entegrasyonu ve intent algılama
- [`database.py`](client_test.py): SQLite veritabanı işlemleri
- [`.env`](.env): Google API anahtarı
- [`requirements.txt`](requirements.txt): Gerekli paketler

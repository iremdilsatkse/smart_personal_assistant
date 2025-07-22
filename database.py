import sqlite3
import os

# Veri tabanı dosyasının yolu
DB_PATH = os.path.join("data", "assistant.db")

# Veri tabanını başlatan fonksiyon
def initialize_db():
    # data klasörü yoksa
    os.makedirs("data", exist_ok=True)

    # veri tabanına bağlanma
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # notes tablosu yoksa 
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS notes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        content TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   
                    )
                """)

    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS calendar (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        event TEXT NOT NULL,
                        event_date TEXT NOT NULL
                    )
                """)

    # Değişiklikleri kaydetme
    conn.commit()

    # Bağlantıyı kapatma
    conn.close()

# Veri tabanına yeni not ekleme
def add_notes(content):
    # Veri tabanına bağlantı kurma
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Content'i notes tablosuna ekleme işlemi
    cursor.execute("INSERT INTO notes (content) VALUES (?)", (content,))

    # Değişiklikleri kaydetme
    conn.commit()

    # Bağlantıyı kapatma
    conn.close()

# Yeni bir etkinlik ekleme
def add_event(event, event_date):
    # Veri tabanına bağlantı kurma
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Etkinlik ve tarih bilgilerini calendar tablosuna ekleme işlemi
    cursor.execute("INSERT INTO calendar (event, event_date) VALUES (?, ?)", (event, event_date))

    # Değişiklikleri kaydetme
    conn.commit()

    # Bağlantıyı kapatma
    conn.close()

# Tüm notları veri tabanından sıralı şekilde getirme
def get_notes():
    # Veri tabanına bağlantı kurma
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # "notes" tablosundan içerik ve tarih bilgilerini alma işlemi
    cursor.execute("SELECT content, created_at FROM notes ORDER BY created_at DESC")

    # Sonuçları liste olarak alma
    notes = cursor.fetchall()

    # Değişiklikleri kaydetme
    conn.commit()

    # Bağlantıyı kapatma
    conn.close()

    return notes

# Tüm etkinlikleri veri tabanından sıralı şekilde getirme
def get_events():
    # Veri tabanına bağlantı kurma
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # "calendar" tablosundan etkinlikleri ve tarih bilgilerini alma işlemi
    cursor.execute("SELECT event, event_date FROM calendar ORDER BY event_date DESC")

    # Sonuçları liste olarak alma
    events = cursor.fetchall()

    # Değişiklikleri kaydetme
    conn.commit()

    # Bağlantıyı kapatma
    conn.close()

    return events

if __name__ == "__main__":
    initialize_db()
    add_notes("mail kontrol etmeyi unutma")
    add_event("w-code açılış toplantısı var", "22.07.2025")

    print(f"Notes: {get_notes()}")
    print(f"Events: {get_events()}")























"""
Gemini kullanarak akıllı asistan oluşturma.
Notlar, görevler, etkinlikler gibi kişisel ihtiyaçlar için akıllı asistan.
    - Bilgi özetleme, bilgi çıkarma, takvim oluşturma gibi özelliklere sahip.
"""
"""
Gemini 2.0 Flash modeli kullanıldı.
"""
from assistant import get_gemini_response, detect_intent
from database import initialize_db, add_notes, add_event, get_notes, get_events

initialize_db()

print("Akıllı Asistana Hoşgeldiniz")
print("Komutlar: Not Ekle | Etkinlik Ekle | Notları Göster | Etkinlikleri Göster | Sohbet Et | Çıkış")

while True:
    command = input("Komut girin: ").strip().lower()

    if command == "not ekle":
        content = input("Not içeriği nedir?: ")
        add_notes(content)
        print("Not başarıyla kaydedildi. ")

    elif command == "etkinlik ekle":
        event = input("Etkinlik içeriği nedir?: ")
        date = input("Etkinlik tarihi nedir?: ")
        add_event(event, date)
        print("Etkinlik başarıyla eklendi. ")

    elif command == "notları göster":
        notes = get_notes()
        if notes:
            print("Notlar: ")
            for content, created_at in notes:
                print(f"- [{created_at}] {content}")
        else:
            print("Henüz bir not eklenmedi.")

    elif command == "etkinlikleri göster":
        events = get_events()
        if events:
            print("Etkinlikler: ")
            for event, event_date in events:
                print(f"- [{event_date}] {event}")
        else:
            print("Henüz bir etkinlik eklenmedi.")

    elif command == "sohbet et":
        message = input("Kullanıcı: ").strip()
        intent = detect_intent(message)

        if intent == "not_ozet":
            notes = get_notes()
            if not notes:
                print("Henüz özetlenecek not bulunmuyor.")
                continue

            all_notes_text = "\n".join([f"- {note[0]}" for note in notes])
            prompt = f"Aşağıda bulunan notları özetle \n\n {all_notes_text}"
            summary = get_gemini_response(prompt)

            print("Not Özeti: \n")
            print(summary)

        elif intent == "etkinlik_ozet":
            events = get_events()
            if not events:
                print("Henüz özetlenecek etklinlik bulunmuyor.")
                continue

            all_events_text = "\n".join([f"- {event[1]}: {event[0]}" for event in events])
            prompt = f"Aşağıda bulunan etkinlikleri kullanıcı isteğine göre özetle \n\n {all_events_text}\n\n kullanıcı isteği: {message}"
            summary = get_gemini_response(prompt)

            print("Etkinlik Özeti: \n")
            print(summary)

        else:
            reply = get_gemini_response(message)
            print(f"Akıllı Asistan: {reply}")

    elif command == "Çıkış":
        break

    else:
        print("Hatalı komut girdiniz.")


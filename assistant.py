import os
import requests 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY .env dosyasında tanımlı değil. ")

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

# API çağrısı için gerekli http başlıkları
headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": api_key
}

# Sorunun cevaplandığı fonksiyon
def get_gemini_response(prompt: str) -> str:
    payload = {
        "contents": [
            {
                "parts": [
                {
                    "text": prompt
                }
                ]
            }
        ]
    }

    # Gemini API'ye http post isteği
    response = requests.post(url, headers = headers, json = payload)

    # İstek başarılıysa
    if response.status_code == 200:
        try:
            result = response.json()
            return result["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            return f"Yanıt Hatası: {e}"
    else:
        return f"API Hatası: {response.status_code}: {response.text}"

# Kullanıcı mesjaına göre sınıflandırma
def detect_intent(message):
    prompt = f"""
                Kullancıının aşağıdaki cümlesini sınıflandır:

                Etiketlerden sadece birini döndür:
                - not_ozet (eğer notları özetlemesini istiyorsa)
                - etkinlik_ozet (eğer etkinlikleri görmek ya da özet istiyorsa)
                - normal (diğer her şey)

                Cümle: "{message}"
                Yalnızca etiket döndür: (örnek: not_ozet)
            """
    
    response = get_gemini_response(prompt)
    return response.strip().lower()


if __name__ == "__main__" :
    user_input = input("Sorunuz: ")
    output = get_gemini_response(user_input)
    print(f"Akıllı Asistan Yanıtı: {output}")













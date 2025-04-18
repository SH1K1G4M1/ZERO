from fbchat import Client, Message
from fbchat.models import ThreadType
import time

# Cookies Facebook Anda
cookies = {
    "dbln": "%7B%2261550534434791%22%3A%22fDTK4Pdo%22%7D",
    "datr": "i23yZ5QVh94nWz65iwd3zYX6",
    "sb": "jG3yZxGK1cYJxxZSwWPYdZVT",
    "ps_l": "1",
    "ps_n": "1",
    "locale": "id_ID",
    "m_pixel_ratio": "2",
    "wd": "360x666",
    "c_user": "61550534434791",
    "fr": "0o5xJusWFTyQNb05a.AWfcVVLRx0iBu2DyZ-_pY54ghfslT5k_On6d8twvKYrfZzCEfyc.Bn8m2M..AAA.0.0.BoAn5f.AWfgTv1J9_bMOFAUaNWXvHZ9tQY",
    "xs": "14%3AO54baFlLafLoog%3A2%3A1744993887%3A-1%3A10884",
    "fbl_st": "100634330%3BT%3A29083231",
    "vpd": "v1%3B666x360x2",
    "wl_cbv": "v2%3Bclient_version%3A2791%3Btimestamp%3A1744993892"
}

class AutoResponderBot(Client):
    def onMessage(self, mid=None, author_id=None, message=None, thread_id=None,
                  thread_type=ThreadType.USER, **kwargs):
        # Jangan balas pesan sendiri
        if author_id == self.uid:
            return

        msg_text = message.lower()
        
        if "list" in msg_text:
            response = """>OPEN
• MURBUG
Mulai dari 20k/Minggu

• JASA BUG
Mulai dari 5k/Nomor

• DAN PRICE PANEL
Mulai dari 10k/Unli

• PEMBUATAN BOT
Mulai dari 50k Tergantung Request Pembeli

Apa itu virtex dan bug? Semacam text yang berat untuk diproses WhatsApp mengakibatkan WhatsApp C1 Force Close di HP target
Order Sung Ke PM 🔥

Untuk Jasa Buat Sc Ngotak dikit Jangan banyak minta kalo budget dikit"""

            self.send(Message(text=response), thread_id=thread_id, thread_type=thread_type)

if __name__ == "__main__":
    try:
        client = AutoResponderBot(session_cookies=cookies)
        print("Bot berhasil login!")
        client.listen()
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Pastikan cookies masih valid!")
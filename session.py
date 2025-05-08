# Yeni bir Python dosyası oluşturun (session.py)
from pyrogram import Client

# API bilgilerinizi girin
api_id = "22997173"
api_hash = "68df0f71d6a8978a5c1f11dfb5f9e4df"

# Client oluşturun
app = Client("my_account", api_id=api_id, api_hash=api_hash)

# Session'ı başlatın
with app:
    print(app.export_session_string())
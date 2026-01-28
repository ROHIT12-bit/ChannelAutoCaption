import os
import time
import threading
import logging
from flask import Flask

from pyrogram import Client, idle
from config import Config

# --- logging ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# --- Web server (Render needs an open port) ---
web = Flask(__name__)

@web.get("/")
def home():
    return "✅ Bot is alive"

def run_web():
    port = int(os.environ.get("PORT", "10000"))
    web.run(host="0.0.0.0", port=port)

# --- Bot ---
class autocaption(Client):
    def __init__(self):
        super().__init__(
            name="Captioner",          # ✅ in pyrogram 1.4.0 use name= not session_name=
            bot_token=Config.BOT_TOKEN,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            workers=20,
            plugins=dict(root="plugins"),
        )

if __name__ == "__main__":
    # Start web server first so Render detects the port
    threading.Thread(target=run_web, daemon=True).start()
    time.sleep(1)

    app = autocaption()
    app.start()
    print("🤖 Bot started")
    idle()
    app.stop()

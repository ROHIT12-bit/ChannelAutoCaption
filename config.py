import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8277167999:AAEuiEqwdpl3m0ZzRaaGgkTwHGFEIjFQn28")
    API_ID = int(os.environ.get("API_ID", 20366634))
    API_HASH = os.environ.get("API_HASH", "72095ec36984aa9ceb0dbaa9cec31559")
    DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://rohitreddyathuru:R6Co7MOjTYQOAqcq@cluster0.xrwjpl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

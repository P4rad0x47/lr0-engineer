from flask import Flask
import redis

app = Flask(__name__)
# Жестко прописываем хост, порт и таймаут
db = redis.Redis(host="redis", port=6379, socket_connect_timeout=5, decode_responses=True)

@app.route("/")
def index():
    try:
        hits = db.incr("hits")
        return f"Привет из Цифрового города! Страницу открывали {hits} раз.\n"
    except Exception as e:
        return f"Ошибка: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
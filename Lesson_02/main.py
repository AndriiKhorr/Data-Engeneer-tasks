print("🚀 Старт main.py")

from flask import Flask, request, jsonify
print("✅ Flask імпортовано")

from job.fetch_sales import fetch_sales_data
print("✅ fetch_sales імпортовано")

import os

# 🔧 Ініціалізація Flask
app = Flask(__name__)
print("✅ Flask app створено")

@app.route("/run-job", methods=["POST"])
def run_job():
    data = request.get_json()
    print("📩 Отримано POST-запит:", data)

    raw_dir = data.get("raw_dir")
    if not raw_dir:
        return jsonify({"error": "Missing 'raw_dir' in request"}), 400

    try:
        fetch_sales_data(raw_dir)
        return jsonify({
            "status": "success",
            "message": f"Data saved to {raw_dir}"
        }), 200

    except Exception as e:
        print(f"❌ Помилка в fetch_sales_data: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# ▶️ Запуск Flask-сервера
if __name__ == "__main__":
    try:
        print("🟡 Запускаємо Flask-сервер...")
        app.run(port=8081)
    except Exception as e:
        print("🔥 Сталася помилка при запуску Flask:")
        print(e)

import requests

# 🔗 URL локального Flask-сервера
url = "http://127.0.0.1:8081/run-job"

# 📁 Каталог, куди зберігати sales-файли
data = {
    "raw_dir": "Lesson_02/raw/sales"
}

# 📤 Відправка POST-запиту
try:
    response = requests.post(url, json=data)
    print("✅ Відповідь від сервера:")
    print(response.status_code)
    print(response.json())
except Exception as e:
    print(f"❌ Помилка при запиті: {e}")

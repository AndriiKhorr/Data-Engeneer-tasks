import requests

url = "https://fake-api-vycpfa6oca-uc.a.run.app/sales?page=1"
token = "2b8d97ce57d401abd89f45b0079d8790edd940e6"

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)

print("Статус:", response.status_code)
print("Тіло:", response.text)

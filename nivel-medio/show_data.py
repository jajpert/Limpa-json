import requests

response = requests.get("http://localhost:5000/api/usuarios")

if response.status_code == 200:
    usuarios = response.json()
    for usuario in usuarios:
        print(usuario)
else:
    print("Falha ao obter dados:", response.text)

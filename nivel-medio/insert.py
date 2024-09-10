import json
import re
import requests
from datetime import datetime

data = """
{
  "usuarios": [
    {
      "id": "1a",
      "nome": "Ana Souza",
      "idade": "24 anos",
      "email": "ana_souza!email.com",
      "telefone": "+55(11)98765-4321",
      "endereco": "Rua A, 123",
      "data_cadastro": "2023-15-10",
      "ativo": "yes",
      "salario": "4500.50"
    },
    {
      "id": 2,
      "nome": "Carlos Pereira",
      "idade": -30,
      "email": "carlos.pereira@dominio",
      "telefone": "11987654321",
      "endereco": null,
      "data_cadastro": "2021-02-30",
      "ativo": "true",
      "salario": "quatro mil"
    },
    {
      "id": 3,
      "nome": "",
      "idade": 29,
      "email": "bianca@example.com",
      "telefone": null,
      "endereco": "Rua B, 45",
      "data_cadastro": "2022-06-15",
      "ativo": "nÃ£o",
      "salario": 3200.00
    },
    {
      "id": "quatro",
      "nome": "Lucas Oliveira",
      "idade": "trinta",
      "email": "lucas.oliveira@site",
      "telefone": "11 98765 4321",
      "endereco": "Av. Principal, 999",
      "data_cadastro": "2020-31-31",
      "ativo": 1,
      "salario": 5000
    },
    {
      "id": 5,
      "nome": "Maria Fernanda",
      "idade": "25",
      "email": "maria#example.com",
      "telefone": "98(8765)4321",
      "endereco": "Rua C, 67",
      "data_cadastro": "2023-08-09",
      "ativo": "Y",
      "salario": "4000"
    },
    {
      "id": null,
      "nome": "Pedro Martins",
      "idade": "22",
      "email": "pedro.martins@",
      "telefone": "98532",
      "endereco": "Estrada Velha, km 45",
      "data_cadastro": "2024-04-01",
      "ativo": "sim",
      "salario": null
    }
  ]
}
"""


def clean_data(data):
    cleaned_data = []
    for i, user in enumerate(data["usuarios"]):

        if not isinstance(user["id"], int):
            user["id"] = i + 1

        try:
            user["idade"] = int(re.sub(r"\D", "", str(user["idade"])))
        except ValueError:
            user["idade"] = None

        if (
            not re.match(r"[^@]+@[^@]+\.[^@]+", user["email"])
            or ".com" not in user["email"]
        ):
            user["email"] = None

        user["telefone"] = re.sub(r"\D", "", str(user["telefone"]))
        if len(user["telefone"]) < 11:
            user["telefone"] = None

        try:
            user["data_cadastro"] = datetime.strptime(
                user["data_cadastro"], "%Y-%m-%d"
            ).date()
        except ValueError:
            user["data_cadastro"] = None

        user["ativo"] = user["ativo"] in ["yes", "true", "1", "Y", "sim"]

        try:
            user["salario"] = float(re.sub(r"[^\d.]", "", str(user["salario"])))
        except ValueError:
            user["salario"] = None

        if user["data_cadastro"]:
            user["data_cadastro"] = user["data_cadastro"].isoformat()

        if not user["nome"]:
            continue

        cleaned_data.append(user)
    return cleaned_data


data = json.loads(data)

cleaned_data = clean_data(data)

response = requests.post("http://localhost:5000/api/usuarios", json=cleaned_data)

if response.status_code == 200:
    print("Dados enviados com sucesso!")
else:
    print("Falha ao enviar dados:", response.text)

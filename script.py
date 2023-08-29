import pip._vendor.requests as requests

def fetch_car_model(model_id):
    url = f"http://localhost:3000/carros/{model_id}" 
    response = requests.get(url)

    if response.status_code == 200:
        car_model = response.json()
        return car_model
    elif response.status_code == 404:
        print("Modelo não encontrado.")
        return None
    else:
        print("Erro ao recuperar os dados:", response.status_code)
        return None

model_id = 1 

carro = fetch_car_model(model_id)

if carro:
    print("Modelo:", carro["modelo"])
    print("Fabricante:", carro["fabricante"])
    print("Ano:", carro["ano"])
    print("Motor:", carro["motor"]["tipo"])
    print("Potência do Motor:", carro["motor"]["potencia_hp"], "HP")
    print("Transmissão:", carro["transmissao"])
    print("Cores Disponíveis:", ", ".join(carro["cores_disponiveis"]))
    print("Preço:", carro["preco"])
else:
    print("Nenhum dado de carro disponível.")

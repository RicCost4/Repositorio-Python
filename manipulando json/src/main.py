import json

data_JSON = """
{
    "size": "Medium",
    "price": 15.67,
    "toppings": ["Mushrooms", "Extra Cheese", "Peperoni", "Basil"],
    "client": {
        "name": "Jane Doe",
        "phone": "455-344-234",
        "email": "jane@teste.com"
    }
}
"""
# dict_json = json.loads(data_JSON)  # transforma um formato json em dicionario

# print(dict_json)

# # tranforma dicionario em json com formato de print em console.
# json_json = json.dumps(dict_json, indent=4)

# print(json_json)

# ler um arquiv json e importa num dicionario.
with open("path.json") as file:
    data = json.load(file)
    # print(data)

    for order in data["lista"]:
        # print(order)
        for valor in order.values():
            # print(valor)
            if "comando" in order:
                print(order["comando"])
    # excluir uma condição do dicionario importado.
    # for order in data["orders"]:
    #     del order["client"]

# escrever as novas mudunças em um novo json
# with open("order_new.json", "w") as file:
    # json.dump(data, file, indent=4)

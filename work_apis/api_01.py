import requests

URL = "https://api.exemplo.com/usuarios"

# Função para listar usuários (GET)
def list_user():
    resposta = requests.get(URL)
    if resposta.status_code == 200:
        for user in resposta.json():
            print(f"Nome: {user['nome']} | Idade: {user['idade']}")
    else:
        print("Erro ao buscar usuários!")

# Funcão para adicionar um novo usuário(POST)
def add_user(name, age):
    dados = {"nome":name, "idade": age}
    resposta = requests.post(URL, json = dados)

    if resposta.status_code == 200:
        print(f"Usuário {name} adicionado com sucesso!")
    else:
        print("Erro ao adicionar usuário.")


# Função para atualizar usuários(PUT)
def update_user(id, new_age):
    dados = {"idade": new_age}
    resposta = requests.put(f"{URL}/{id}", json=dados)
    
    if resposta.status_code == 200:
        print("Usuário atualizado com sucesso!")
    else:
        print("Erro ao atualizar usuário.")

# Função para deletar usuário(DELETE)
def delete_user(id):
    resposta = requests.delete(f"{URL}/{id}")
    if resposta.status_code == 204:
        print("Usuário deletado!")
    else:
        print("Erro ao deletar usuário.")

list_user()
add_user("Eliseu", 24)
update_user(123, 32)
delete_user(123)
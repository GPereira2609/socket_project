import threading
import socket
import json

from bd import mensagens

host = 'localhost'
port = 5000

clientes = []

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((host, port))
        server.listen()
    except:
        return print('\nNão foi possível iniciar o servidor\n')
    
    print(f"Ouvindo....\nHost = {host}\nPorta = {port}")

    while True:
        client, addr = server.accept()
        clientes.append(client)

        thread = threading.Thread(target=tratar_mensagem, args=[client])
        thread.start()

def adicionar_mensagem(msg, client):
    try:
        mensagens.append({
            "id": msg["id"],
            "mensagem": msg["data"]
        })

        msg = {
            "status": 201, "message": "Mensagem criada", "data": ""
        }

        enviar_mensagem(str(msg).encode("utf-8"), client)
    except:
        msg = {
            "status": 401, "message": "Não foi possível adicionar a mensagem", "data": ""
        }
        enviar_mensagem(str(msg).encode('utf-8'), client)

def mostrar_mensagem(msg, client):
    try:
        msg_c = ''
        for msg in mensagens:
            msg_c += f"{msg},"
        msg_c = msg_c[:-1]
        msg_s = {
            "status": 200, "message": "OK", "data": msg_c
        }
        enviar_mensagem(f"{msg_s}\n".encode("utf-8"), client)
    except:
        msg_s = {
            "status": 400, "message": "Não foi possível mostrar as mensagens", "data": ""
        }
        enviar_mensagem(f"{msg_s}\n".encode("utf-8"), client)

def deletar_mensagem(msg, client):
    try:
        ids = []
        for mensagem in mensagens:
            ids.append(mensagem['id'])

        if msg["id"] in ids:
            for m in mensagens:
                if m["id"] == msg["id"]:
                    mensagens.remove(m)
                    msg_s = {
                        "status": 202, "message": "Mensagem deletada", "data": ""
                    }
                    enviar_mensagem(f"{msg_s}".encode("utf-8"), client)
        else:
            msg_s = {
                "status": 402, "message": "ID não existe", "data": ""
            }
            enviar_mensagem(f"{msg_s}".encode("utf-8"), client)
    except:
        msg_s = {
            "status": 403, "message": "Não foi possível deletar a mensagem", "data": ""
        }
        enviar_mensagem(f"{msg_s}".encode("utf-8"), client)

def tratar_mensagem(client):
    while True:
        try:
            msg = client.recv(2048)
            n_msg = msg.decode("utf-8")
            n_msg = json.loads(msg)

            if n_msg["op"] == "adicionar":
                adicionar_mensagem(n_msg, client)

            elif n_msg["op"] == "mostrar":
                mostrar_mensagem(n_msg, client)

            elif n_msg["op"] == "deletar":
                deletar_mensagem(n_msg, client)
                
            else:
                print("falha")
                enviar_mensagem("falha", client)
        except:
            deletar_cliente(client)
            break


def enviar_mensagem(msg, client):
    for cli in clientes:
        if cli == client:
            try:
                cli.send(msg)
            except:
                deletar_cliente(cli)


def deletar_cliente(client):
    clientes.remove(client)

if __name__ == "__main__":
    main()
import threading
import socket

host = 'localhost'
port = 5000

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((host, port))
    except:
        return print('\nA conexão não pôde ser estabelecida\n')

    print(f"\nConexão estabelecida\nHost = {host}\nPorta = {port}")

    thread1 = threading.Thread(target=receber_mensagem, args=[client])
    thread2 = threading.Thread(target=enviar_mensagem, args=[client])

    thread1.start()
    thread2.start()


def receber_mensagem(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(f"{msg}\n")
        except:
            msg = {
                "status": 505, "message": "Conexão encerrada", "data": ""
            }
            print(f'{msg}\n')
            client.close()
            break
            

def enviar_mensagem(client):
    while True:
        try:
            msg = str(input())
            client.send(f'{msg}'.encode('utf-8'))
        except:
            msg = {
                "status": 504, "message": "Erro ao enviar mensagem", "data": ""
            }

            return print(f"\n{msg}")


if __name__ == "__main__":
    main()
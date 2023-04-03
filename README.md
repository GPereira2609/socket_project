# Cliente-servidor com sockets e threads

# Para baixar o servidor 
```
	docker pull gpereira2609/socket-server:socket_project
```
# Para rodar o servidor 
```
	docker run -p 5000:5000 gpereira2609/socket-server:socket_project
	
```
# Para baixar o cliente
```
	docker pull gpereira2609/socket-client:socket_project
```
# Para rodar o cliente
``` 
	docker run -p 5000:5000 gpereira2609/socket-client:socket_project
```

# Interfaces 

# Request:
A requisição é feita em JSON, e precisa ter 3 parâmetros:
id: um inteiro que representará o id do objeto (caso exista)
op: uma string que representará a operação realizada
data: os dados que serão utilizados para criar um objeto
```
	{"id": int, "op": str, "data": str}
```


# Response:
A resposta contém um status, uma mensagem e um campo para dados, conforme o exemplo a seguir:
```
	{"status": int, "message": str, "data": str}
```

# Mensagens possíveis:
# Confirmação:
200: OK
```
	{"status": 200, "message": "OK", "data": ""}
```
201: Mensagem criada
```
	{"status:" 201, "message": "Mensagem criada", "data": ""}
```
202: Mensagem deletada
```
	{"status": 202, "message": "Mensagem deletada", "data": ""}
```

# Erro:
400 Não foi possível mostrar as mensagens
```
	{"status": 400, "message": "Não foi possível mostrar as mensagens", "data": ""}
```
401 Não foi possível adicionar a mensagem
```
	{"status": 401, "message": "Não foi possível adicionar a mensagem", "data": ""}
```
402 ID não existe
```
	{"status": 402, "message": "ID não existe", "data": ""}
```
403 Não foi possível deletar a mensagem
```
	{"status": 403, "message": "Não foi possível deletar a mensagem", "data": ""}
```

# Erro de conexão:
504 Mensagem não foi enviada
```
	{"status": 504, "message": "Mensagem não foi enviada", "data": ""}
```

505 Conexão encerrada
```
	{"status": 505, "message": "Conexão encerrada", "data": ""}
```

# Operações do sistema

# Listar usuários
```
	Requisição: {"op": "mostrar", "id": "", "data": ""}
	
	Resposta: {'status': 200, 'message': 'OK', 'data': "{'id': 1, 'mensagem': 'abc'},{'id': 2, 'mensagem': 'fgh'}"}
	
	Resposta: {"status": 400, "message": "Não foi possível mostrar as mensagens", "data": ""}
```
# Adicionar usuário
```
	Requisição: {"op": "adicionar", "id": 3, "data": "teste"}
	
	Resposta: {'status': 201, 'message': 'Mensagem criada', 'data': ''}
	
	Resposta: {"status": 401, "message": "Não foi possível adicionar a mensagem", "data": ""}
```
# Remover usuário
```
	Requisição: {"op": "deletar", "id": 3, "data": ""}
	
	Resposta: {'status': 202, 'message': 'Mensagem deletada', 'data': ''}
	
	Resposta: {"status": 402, "message": "ID não existe", "data": ""}
	
	Resposta: {"status": 403, "message": "Não foi possível deletar a mensagem", "data": ""}
```

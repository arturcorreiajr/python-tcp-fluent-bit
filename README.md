# Subindo os servicos
Criar imagem docker para o serviç python-tcp usando  o projeto https://github.com/arturcorreiajr/python-tcp.git 

Criar imagem docker para o fluent-bit 
```console 
    docker build -t fluent-bit:latest
```

Informar nome da imagem  do python-tcp  criada no docker-compose 
Executar docker compose
```console 
    docker-compose up -d
```

Acessar container da aplicacao python
```console 
    docker exec -it 5e4accc947cf bash
```

Executar aplicaçāo
```console 
    python3 main.py
```

Preencher inputs
```console 
    Informar host:
    Informar port:
    Mensagem a enviar:
```

Mensagem a enviar no formato json
```console 
    {"message":"Mensagem"}
```



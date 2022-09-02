# Subindo os servicos
Criar imagem docker para o serviç python-tcp usando  o projeto https://github.com/arturcorreiajr/python-tcp.git &nbsp;

Criar imagem docker para o fluent-bit &nbsp;
    '''docker build -t fluent-bit:latest''' &nbsp;

Informar nome da imagem  do python-tcp  criada no docker-compose &nbsp;
Executar docker compose
    '''docker-compose up -d'''

Acessar container da aplicacao python &nbsp;
'''docker exec -it 5e4accc947cf bash''' &nbsp;





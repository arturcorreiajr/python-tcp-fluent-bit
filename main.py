import socket

HOST = '172.19.0.2'           # Endereco IP do Servidor
PORT = 5170                  # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print ('Conectei')
msg = (b'{\"message\":\"OI, eu vim do python em docker\"}')
tcp.send (msg)
tcp.close()
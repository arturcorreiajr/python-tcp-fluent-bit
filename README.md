
Criar imagem docker python usando  o projeto python-tcp

Criar imagem docker para o fluent-bit
docker build -t arturcorreiajunior/fluent-bit-docker:latest .
docker push arturcorreiajunior/fluent-bit:latest
docker run -p 8080:5170 arturcorreiajunior/fluent-bit-docker:latest 

kubectl apply -f yaml/fluent-bit-deploy.yaml

echo '{"message": "Oi, eu vim do TCP"}' | nc 127.0.0.1 8080

docker exec -it 5e4accc947cf bash




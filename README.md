# requestDataCar
Atendendo o desafio proposto pela DIO, uma forma alternativa a ETL, construi um pequeno banco de dados em formato JSON, e um pequeno script em python para fazer um get de modelos de carros disponíveis dentro do BD.
Para rodar o banco de dados eu usei o comando "json-server --watch car_data.json" no terminal. Esse comando criou um pequeno servidor na porta 3000 da minha máquina, fazendo possível a requisição no código em python.
O código, quando executado, mostrará os prints dos detalhes de cada modelo a partir do número id definido na variável "model_id". Caso queira que mostre outro modelo, é so altera-la. No total foram feitos 3 modelos de
carros distintos. 
Nesta aplicação estou somente trabalhando com o método GET, pois ainda é uma área nova que estou conhecendo as funcionalidades.

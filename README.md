# FoodCare API

[![Maintainability](https://api.codeclimate.com/v1/badges/f32161ad0dd11e650c14/maintainability)](https://codeclimate.com/github/fga-eps-mds/2019.2-FoodCare/maintainability)

[Link](https://github.com/fga-eps-mds/2019.2-FoodCare-webapp) do repositório contendo o frontend.

## Configuração do ambiente
### Instalação

É utilizado o docker como forma de configuração de ambiente. Para utilizar o docker basta executar a seguinte linha de código:

Faça o download do Docker CE no [site oficial](https://docs.docker.com/engine/installation/).
Faça o download do Docker Compose no [site oficial](https://docs.docker.com/compose/install/).

Para construir novamente o container caso tenha feito alguma alteração no código utilize o seguinte comando

```
$ [sudo] docker-compose build
```

### Subindo o servidor

Para subir a aplicação no endereço `0.0.0.0` e na porta 8000 utilize o seguinte comando:

```
$ [sudo] docker-compose up
```

A aplicação estará disponível em `http://localhost:8000`.
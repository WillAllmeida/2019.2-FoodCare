<p align="center">
    <img src="docs/assets/images/id-visual/vertical-normal.png" alt="Logo">
</p>

<h1 align="center">FoodCare API</h1>

<p align="center">
    <a href="https://codeclimate.com/github/fga-eps-mds/2019.2-FoodCare/maintainability" alt="Manutenibilidade" >
        <img src="https://api.codeclimate.com/v1/badges/f32161ad0dd11e650c14/maintainability" />
    </a>
    <a href="https://travis-ci.org/fga-eps-mds/2019.2-FoodCare" alt="Status da build" >
        <img src="https://travis-ci.org/fga-eps-mds/2019.2-FoodCare.svg?branch=master" />
    </a>
    <a href="http://isitmaintained.com/project/fga-eps-mds/2019.2-FoodCare" alt="Porcentagem de issues abertas" >
        <img src="http://isitmaintained.com/badge/open/fga-eps-mds/2019.2-FoodCare.svg" />
    </a>
    <a href="http://isitmaintained.com/project/fga-eps-mds/2019.2-FoodCare" alt="Tempo médio para fechar uma issue" >
        <img src="http://isitmaintained.com/badge/resolution/fga-eps-mds/2019.2-FoodCare.svg" />
    </a>
    <a href="https://www.gnu.org/licenses/gpl-3.0" alt="Licença: GPL v3" >
        <img src="https://img.shields.io/badge/License-GPLv3-blue.svg" />
    </a>
</p>

<p align="center">
    <a href="https://github.com/fga-eps-mds/2019.2-FoodCare-WebApp"><strong>Acesse FoodCare WebApp</strong></a>
</p>

<p align="center">
    <a href="https://fga-eps-mds.github.io/2019.2-FoodCare"><strong>Acesse FoodCare Docs</strong></a>
</p>

## Sobre o projeto

**FoodCare** é um sistema online que gerencia o encontro entre doadores de alimento, com pessoas e ONGs que precisam desse alimento. Nosso propósito é evitar que pessoas, ou empresas, joguem fora alimentos que ainda são próprios para consumo, conectando-as com quem precisa desses alimentos, ajudando a combater a fome no Brasil.

## Funcionalidades principais

- Cadastro de Doadores
- Gerenciamento de Eventos
- Mapa e Lista de Eventos
- Notificação de Eventos

## Tecnologias utilizadas

**Desenvolvido com** [Django](https://www.djangoproject.com/)  
**Conteinerizado com** [Docker](https://www.docker.com/)  

## Instalação

É utilizado o docker como forma de configuração de ambiente. Para utilizar o docker basta executar a seguinte linha de código:

Faça o download do Docker CE no [site oficial](https://docs.docker.com/engine/installation/).
Faça o download do Docker Compose no [site oficial](https://docs.docker.com/compose/install/).

Para construir novamente o container caso tenha feito alguma alteração no código utilize o seguinte comando:

```bash
[sudo] docker-compose build
```

## Execução

Para subir a aplicação no endereço `0.0.0.0` e na porta 8000 utilize o seguinte comando:

```bash
[sudo] docker-compose up
```

A aplicação estará disponível em `http://localhost:8000`.

<!-- ## Testes

Descreva e mostre como rodar testes. -->

## Contribuição

Siga o [guia de contribuição](CONTRIBUTING.md) e o [código de conduta](CODE_OF_CONDUCT.md) para entender os passos e regras para adicionar sua contribuição ao projeto.

## Licença

GPLv3 © FoodCare. Acesse a [licença](LICENSE) para mais detalhes.

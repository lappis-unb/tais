---
layout: page
permalink: /documentacao/como-rodar/
title: Como rodar a Tais em seu computador
---

A Tais possui vários ambientes e vários componentes para rodar. Veja e entenda todos eles:

1. [Subir com RocketChat](#rocketchat)
2. [Subir somente o console](#console)
3. [Subir site para Beta Testers](#site-do-beta)
4. [Subir o Analytics](#analytics)
5. [Subir Dashboard do Kibana](#dashboards-visualização-do-kibana)
6. [Subir Notebooks](#notebooks-análise-de-dados)
7. [QuickStart - Subir toda a Stack](#quickstart)
8. [Documentação](#documentação)


## Subindo o chatbot
### RocketChat
Para testar a Tais utilizando da plataforma do RocketChat, siga os seguintes comandos para subir os containers em seu computador:

``` sh
sudo docker-compose up -d rocketchat
# aguarde o container subir
sudo docker-compose up bot
```

Após esses comandos o RocketChat deve estar disponível na porta `3000` do seu computador. Entre em `http://localhost:3000` para acessar. Será pedido que faça login. Por padrão é gerado um usuário admin:
*username:* `admin`
*senha:* `admin`


#### Instalação

Para colocar a Tais em um site você precisa inserir o seguinte código em Javascript na sua página:

``` js
<!-- Start of Rocket.Chat Livechat Script -->
<script type="text/javascript">
(function(w, d, s, u) {

    // !!! Mudar para o seu host AQUI !!!
    host = 'http://localhost:3000';
    // !!! ^^^^^^^^^^^^^^^^^^^^^^^^^^ !!!

    w.RocketChat = function(c) { w.RocketChat._.push(c) }; w.RocketChat._ = []; w.RocketChat.url = u;
    var h = d.getElementsByTagName(s)[0], j = d.createElement(s);
    j.async = true; j.src = host + '/packages/rocketchat_livechat/assets/rocketchat-livechat.min.js?_=201702160944';
    h.parentNode.insertBefore(j, h);
})(window, document, 'script', host + '/livechat');
</script>
<!-- End of Rocket.Chat Livechat Script -->
```

**Atenção**: Você precisa alterar a variável `host` dentro do código acima para a url do site onde estará o seu RocketChat.

### Console
Para testar somente o diálogo com o bot, não é necessário rodar o RocketChat. Caso queira apenas rodar a Tais pelo seu terminal, rode os seguintes comandos:

```sh
sudo docker-compose run --rm bot make train
sudo docker-compose run --rm bot make run-console
```

Essa forma de rodar trás também os logs e previsão de intents do Rasa.


## Site do Beta
Nesse repositório temos também o site para beta testers da Tais. Ele se conecta com a Tais via RocketChat, então para ela estar hospedada é necessário [subir o RocketChat](#RocketChat).

### Setup
Antes de rodá-lo é necessário fazer algumas configurações e criar um usuário. Para isso rode os comandos abaixo e crie o seu usuário.

```
sudo docker-compose run --rm web python manage.py migrate
sudo docker-compose run --rm web python manage.py createsuperuser
```

### Execução
Para rodar o site em `localhost` suba o container com esse comando:
```
sudo docker-compose up -d web
```

Você pode acessar o site por padrão na url `http://localhost:8000`. Será necessário fazer o login, com o usuário criado, esse usuário é um super usuário, então ele tem acesso a parte admin, que poderá ser acessada em `http://localhost:8000/admin/` e poderá criar novos usuários.

## Analytics
Para a análise dos dados das conversas com o usuário, utilize o kibana, e veja como os usuários estão interagindo com o bot, os principais assuntos, média de usuários e outras informações da análise de dados.

### Setup

Para subir o ambiente do kibana rode os seguintes comandos:

```
sudo docker-compose run --rm -v $PWD/analytics:/analytics bot python /analytics/setup_elastic.py
sudo docker-compose up -d elasticsearch
```

Lembre-se de configurar as seguintes variáveis de ambiente no `docker-compose`.

```
ENVIRONMENT_NAME=localhost
BOT_VERSION=last-commit-hash
```

### Visualização

Para visualização do site rode o comando:
```
sudo docker-compose up -d kibana
```

Para acesso do site é necessário fazer o login. Por padrão o usuário criado é `admin` e a senha é `admin`

Você pode acessar o kibana no `http://locahost:5601`

## Dashboards Visualização do Kibana

Dashboards mais básicos do Analytics, sem permissão de `admin`, que disponibilizamos para a Secretaria Especial da Cultura. 

### Setup

Rode as configurações: 
``` sh
sudo docker-compose run --rm kibana-web python manage.py migrate
sudo docker-compose run --rm kibana-web python manage.py createsuperuser
```

### Execução
Para visualização do site, rode o comando:
``` sh
sudo docker-compose up -d kibana-web
```
Você pode acessar o site por padrão na url `http://localhost:8080`


## Notebooks - Análise de dados
Para análise de como estão as intents e stories construidas, se está havendo alguma confusão por intents similares ou outros problemas, utilize os notebooks para gerar os gráficos de matriz de confusão e diagrama da estrutura das stories.

### Setup

Levante o container `notebooks`

```sh
docker-compose up -d notebooks
```

Acesse o notebook em `http://localhost:8888`. Lá entre na pasta `notebooks` e vá para a pasta `intents` ou `stories`, dependendo do que quer analisar, e abra o arquivo `.ipynb`.



## QuickStart

A Tais, no ambiente de produção, consiste no Rasa, RocketChat, página para Beta Testers e o Kibana. Para levantar todo esse ambiente, use os seguintes comandos:

```sh
sudo docker-compose up -d rocketchat

sudo docker-compose run --rm web python manage.py migrate
sudo docker-compose run --rm web python manage.py createsuperuser
sudo docker-compose up -d web

sudo docker-compose up -d kibana
sudo docker-compose run --rm -v $PWD/analytics:/analytics bot python /analytics/setup_elastic.py

# aguarde os containers serem levantados
sudo docker-compose up -d bot
```

## Documentação
A documentação feita está no github pages, veja no link: [lappis-unb.github.io/tais](http://lappis-unb.github.io/tais)
A documentação se encontra na pasta `docs` deste repositório. É feita com `Jekyll` para o github pages. Para rodar a página em seu computador basta rodar o comando:
```
jekyll serve
```
Acesse a pagina em `http://localhost:4000`.
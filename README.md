# Tais - Assistente Virtual da Cultura
<!-- badges -->

A Taís é uma assistente virtual desenvolvida pelo LAPPIS - Laboratório Avançado de Produção, Pesquisa e Inovação em Software (FGA/UnB), em parceria com o Ministério da Cultura. O nome é uma sigla para Tecnologia de Aprendizado Interativo do Salic. 

Esse repositório contém o código do framework do chatbot Tais, composto por:
* **Bot:** Inteligencia artificial do próprio bot, feito em Rasa.
* **Analytics:** Sistema de analise das conversas dos usuários com o chatbot, feito com o Kibana.
* **Notebooks:** Notebooks Jupyter para a analise da estrutura do chatbot.
* **Web:** Página com verificação de usuário para BetaTesters.
---
<!-- Links uteis: -->
* **O que é a Tais? 🤔** [Conheça a Tais](https://github.com/lappis-unb/tais/wiki)

* **O que é o Lappis? ✏️** [Conheça o Lappis](https://lappis-unb.gitlab.io)

* **Estou preparado para testar a Tais! 💻** [Teste a tais em produção](http://rouanet.cultura.gov.br)

* **Como posso rodar a Tais no meu computador? ❓** [Veja como subir o ambiente de desenvolvimento da Taís](#Como-rodar-a-TAIS)

* **Gostaria de Contribuir! 🤗** [Veja como contribuir]()

---

# Como conseguir ajuda

Parte da documentação técnica do framework da Tais está disponível na [wiki do repositório](https://github.com/lappis-unb/tais/wiki). Caso não encontre sua resposta, abra uma issue que tentaremos responder o mais rápido possível.

Também estamos presentes no grupo [Telegram Rasa Stack Brasil](https://t.me/RasaBrasil).

# Como Contribuir

Ficaremos muito felizes de receber e incorporar suas contribuições. Tem algumas informações adicionais sobre o estilo do código e a documentação.

Em geral o processo é bem simples:

- Crie uma issue descrevendo uma feature  que você queira trabalhar (ou olhe as issues com o label `help wanted` e `good-first-issue`)
- Escreva seu código, testes e documentação 
- Abra um pull request descrevendo as suas alterações propostas
- Seu pull request será revisado por um dos mantenedores, que pode levantar questões para você sobre eventuais mudanças necessárias ou questões. 

Leia o código de [Conduta]() e [Contribuição]() para melhores informações.


# Como Rodar a TAIS

## Subindo o chatbot

### RocketChat
Para testar a Tais utilizando da plataforma do Rocket Chat, siga os seguintes comandos para subir os containers em seu computador:

```sh
sudo docker-compose up -d rocketchat
# aguarde 3 minutos para o rocketchat terminar de levantar
sudo docker-compose up bot
```

Apos esses comandos o Rocket Chat deve estar disponivel na porta `3000`do seu computador. Entre em `http://localhost:3000` para acessar. Será pedido que faça login. Por padrão é gerado um usuário admin:
*username:* `admin`
*senha:* `admin`

Para que a assistente virtual inicie a conversa você deve criar um `trigger`.
Para isso, entre no rocketchat como `admin`, e vá no painel do Livechat na
seção de Triggers, clique em `New Trigger`. Preencha o Trigger da seguinte forma:

```yaml
Enabled: Yes
Name: Start Talk
Description: Start Talk
Condition: Visitor time on site
    Value: 3
Action: Send Message
 Value: Impersonate next agent from queue
 Value: Olá, meu nome é Taís, sou assistente virtual do MinC! Você quer conversar sobre incentivo à cultura? 
```

O valor `http://localhost:8080/` deve ser a URL de acesso da Taís.

#### Instalação

Para colocar a Taís em um site você precisa inserir o seguinte Javascript na sua página

```js
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

**Atenção**: Você precisa alterar a variavel `host` dentro do código acima para a url do site onde estará o seu Rocket.Chat.

### Console
Para testar somente a conversação do bot, não é necessário rodar o RocketChat. Caso queira apenas rodar a Tais pelo seu terminal, rode os seguintes comandos:

```sh
sudo docker-compose run --rm bot make train
sudo docker-compose run --rm bot make run-console
```

Essa forma de rodar tras também os logs e previsão de intents do Rasa.

### Train Online

```
sudo docker-compose run --rm bot make train
sudo docker-compose run --rm bot make train-online
```


## Site do Beta

### Setup

```
sudo docker-compose run --rm web python manage.py migrate
sudo docker-compose run --rm web python manage.py createsuperuser
```

### Execução

```
sudo docker-compose up -d web
```

Você pode acessar o site por padrão na url `localhost:8000`




## Analytics

### Setup

```
sudo docker-compose run --rm -v $PWD/analytics:/analytics bot python /analytics/setup_elastic.py
sudo docker-compose up -d elasticsearch
```

Lembre-se de setar as seguintes variáveis de ambiente no `docker-compose`.

```
ENVIRONMENT_NAME=localhost
BOT_VERSION=last-commit-hash
```

### Vizualização

```
sudo docker-compose up -d kibana
```

Você pode acessar o kibana no `locahost:5601`


## Notebooks - Análise de dados

### Setup

Levante o container `notebooks`

```sh
docker-compose up -d notebooks
```

Acesse o notebook em `localhost:8888`



## Como para levantar toda a stack

```sh
sudo docker-compose up -d rocketchat

sudo docker-compose run --rm web python manage.py migrate
sudo docker-compose run --rm web python manage.py createsuperuser
sudo docker-compose up -d web

sudo docker-compose up -d kibana
sudo docker-compose run --rm -v $PWD/analytics:/analytics bot python /analytics/setup_elastic.py

# aguarde 3 minutos para o rocketchat terminar de levantar
sudo docker-compose up -d bot
```


# Passos necessários para gerar uma nova release

A criação de uma nova versão Release é bem simples. Os seguintes passos são necessários para lançar uma nova versão

- edite o CHANGELOG.rst, crie uma nova seção para a release e crie uma nova master loggins section
- Edite o guia de migração para dar assistência para usuários atualizarem para a nova versão
- Commite todas as mudanças acima e gere uma tag para a nova versão usando

```sh
git tag -f 0.7.0 -m "Some helpful line describing the release"
git push origin 0.7.0
```


# Licença

Todo o framework da Tais é desenvolvido sob a licença [GPL3](https://github.com/lappis-unb/tais/blob/master/LICENSE)

Uma lista da lista de dependência das licenças do projeto podem ser encontradas [aqui](https://github.com/lappis-unb/tais/network/dependencies)

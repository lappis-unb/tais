

# Tais - Assistente Virtual da Cultura
<!-- badges -->
<a href="https://www.gnu.org/licenses/gpl-3.0.pt-br.html"><img src="https://img.shields.io/badge/licence-GPL3-green.svg"/></a>
<a href="https://codeclimate.com/github/lappis-unb/tais/maintainability"><img src="https://api.codeclimate.com/v1/badges/64786c126eb53a061bb6/maintainability" /></a>
<a href="https://gitlab.com/lappis-unb/services/tais/-/jobs"><img src="https://gitlab.com/lappis-unb/services/tais/badges/master/pipeline.svg" /></a>

A Taís é uma assistente virtual desenvolvida pelo LAPPIS - Laboratório Avançado de Produção, Pesquisa e Inovação em Software (FGA/UnB), em parceria com o Ministério da Cultura. O nome é uma sigla para Tecnologia de Aprendizado Interativo do Salic.

Esse repositório contém o código do framework do chatbot Tais, composto por:
* **Bot:** Inteligencia artificial do próprio bot, feito em Rasa.
* **Analytics:** Sistema de análise das conversas dos usuários com o chatbot, feito com o Kibana.
* **Notebooks:** Notebooks Jupyter para a análise da estrutura do chatbot.
* **Web:** Página com verificação de usuário para Beta Testers.
---
<!-- Links uteis: -->
* **O que é a Tais? 🤔** [Conheça a Tais](#o-que-é-a-tais)
* **Quero ler a documentação! 📚** [Acesse nosso GitHub Pages](https://lappis-unb.github.io/tais/) e [veja a nossa wiki](https://github.com/lappis-unb/tais/wiki)
* **O que é o Lappis? ✏️** [Conheça o Lappis](https://lappis.rocks)
* **Estou preparado para testar a Tais! 💻** [Teste a tais em produção no Portal da Lei Rouanet](http://rouanet.cultura.gov.br) ou [veja ela em produção em nosso github pages](http://lappis-unb.github.io/tais)
* **Como posso rodar a Tais no meu computador? ⚙️** [Veja e entenda como subir cada parte do ambiente de desenvolvimento da Taís](#Como-rodar-a-TAIS) ou [simplesmente rode os comandos do QuickStart](#QuickStart)
* **Estou com dúvidas... ❓** [Veja como conseguir ajuda](#Como-conseguir-ajuda)
* **Gostaria de Contribuir! 🤗** [Veja como contribuir](#Como-Contribuir)

---
# O que é a Tais?
A Tais é um chatbot desenvolvido pelo [LAPPIS](https://lappis.rocks) junto com a [Secretaria Especial da Cultura](http://www.cultura.gov.br) para o projeto da Lei Rouanet. A Lei Rouanet é o principal mecanismo de fomento a cultura do Brasil, e a Tais tem o objetivo de ajudar os proponentes nos momentos de dúvida. Para saber mais sobre o que é a Lei Rouanet, SALIC e como funciona todo o processo acesse o [Portal da Lei Rouanet](http://rouanet.cultura.gov.br/) lá Tais está em produção e também pode explicar esses conceitos.


# Entenda a Arquitetura

É utilizado na Tais diversas tecnologias que interagem entre si para obter um melhor resultado. Veja a arquitetura implementada:

![](https://user-images.githubusercontent.com/8556291/57933140-d8d66b80-7892-11e9-8d58-a7eda60b099b.png)

O usuário interage com a Tais via RocketChat, que manda as mensagens para o Rasa NLU, que identifica a *intent*, e responde pelo Rasa Core, de acordo com as *stories* e *actions*.
Os notebooks avaliam o funcionamento de acordo com o formato das *intents* e *stories*.
O elasticsearch coleta os dados da conversa e armazena para a análise feita pelo kibana, que gera gráficos para avaliação das conversas dos usuários e da Tais.

# Como Rodar a TAIS
## Subindo o chatbot
### RocketChat
Para testar a Tais utilizando da plataforma do RocketChat, siga os seguintes comandos para subir os containers em seu computador:

```sh
sudo docker-compose up -d rocketchat
# aguarde o container subir
sudo docker-compose up bot
```

Após esses comandos o RocketChat deve estar disponível na porta `3000` do seu computador. Entre em `http://localhost:3000` para acessar. Será pedido que faça login. Por padrão é gerado um usuário admin:
*username:* `admin`
*senha:* `admin`


#### Instalação

Para colocar a Tais em um site você precisa inserir o seguinte código em Javascript na sua página:

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

**Atenção**: Você precisa alterar a variável `host` dentro do código acima para a url do site onde estará o seu RocketChat.

### Console
Para testar somente o diálogo com o bot, não é necessário rodar o RocketChat. Caso queira apenas rodar a Tais pelo seu terminal, rode os seguintes comandos:

```sh
sudo docker-compose run --rm bot make run-console
```

Essa forma de rodar trás também os logs e previsão de intents do Rasa.

### Treinamento
Caso precise atualizar os dialogos com o bot após modificações nas __intents__ e __stories__ (coach/data/intents e stories), utilize o seguinte comando na pasta raiz do projeto para treinar o bot novamente:
```bash
make train
```

Caso queira atualizar o treinamento padrão da aplicação, será necessário atualizar a versão da imagem Coach no dockerhub do lappis:
```bash
make train
sudo docker push lappis/coach:latest
```

## Site do Beta
Nesse repositório temos também o site para beta testers da Tais. Ele se conecta com a Tais via RocketChat, então para ela estar hospedada é necessário [subir o RocketChat](#RocketChat).

### Setup
Antes de rodá-lo é necessário fazer algumas configurações e criar um usuário. Para isso rode os comandos abaixo e crie o seu usuário.

```sh
sudo docker-compose run --rm web python manage.py migrate
sudo docker-compose run --rm web python manage.py createsuperuser
```

### Execução
Para rodar o site em `localhost` suba o container com esse comando:
```sh
sudo docker-compose up -d web
```

Você pode acessar o site por padrão na url `http://localhost:8000`. Será necessário fazer o login, com o usuário criado, esse usuário é um super usuário, então ele tem acesso a parte admin, que poderá ser acessada em `http://localhost:8000/admin/` e poderá criar novos usuários.

## Dashboards Visualização

Dashboards que disponibilizamos para a Secretaria Especial da Cultura.

### Setup

```sh
sudo docker-compose run --rm kibana-web python manage.py migrate
sudo docker-compose run --rm kibana-web python manage.py createsuperuser
```

### Execução

```sh
sudo docker-compose up -d kibana-web
```

Você pode acessar o site por padrão na url `localhost:8080`



## Analytics
Para a análise dos dados das conversas com o usuário, utilize o kibana, e veja como os usuários estão interagindo com o bot, os principais assuntos, média de usuários e outras informações da análise de dados.

### Setup

Para subir o ambiente do ElasticSearch rode os seguintes comandos:

```sh
sudo docker-compose up -d elasticsearch
sudo docker-compose run --rm -v $PWD/analytics:/analytics bot python /analytics/setup_elastic.py
```

Lembre-se de configurar as seguintes variáveis de ambiente no `docker-compose`.

```
ENVIRONMENT_NAME=localhost
BOT_VERSION=last-commit-hash
```

Lembre-se também de configurar como `True` a seguinte variável do serviço `bot` no `docker-compose`.

```
ENABLE_ANALYTICS=False
```

Para habilitar o _backup_ rode o seguinte comando:

```sh
sudo docker exec -it tais_elasticsearch_1 curl -XPUT -H "Content-Type: application/json;charset=UTF-8" 'http://localhost:9200/_snapshot/backup' -d '{
  "type": "fs",
  "settings": {
     "location": "/elasticseacrh/backup",
     "compress": true
  }
}'

# A resposta esperada é: {"acknowledged": true}
```

### Visualização

Para visualização do site rode o comando:
```sh
sudo docker-compose up -d kibana
```

Para acesso do site é necessário fazer o login. Por padrão o usuário criado é `admin` e a senha é `admin`

Você pode acessar o kibana no `http://locahost:5601`

### Para visualização dos Dashboards básico

Visualizações de métricas importantes para o desenvolvimento de chatbots, estão disponibilizados para este contexto.
Para usar estes _templates_ execute os seguintes passos:

* Suba o container do **Kibana** e acesse `http://locahost:5601`;
* Na interface, acesse `Management` e clique em `Saved Objects`;
* Clique em `Import`;
* Utilize o arquivo `export.json` na pasta `elasticsearch/` do projeto.


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

## Testando Fluxos de Conversa

É possível testar os fluxos de conversação utilizando o [Evaluation do Rasa Core](https://github.com/lappis-unb/tais/wiki/Testes-Automatizados). Para testá-los na Tais basta adicionar um arquivo dentro do diretório `bot/e2e/` com as histórias a serem testadas. Essas histórias devem ser descritas normalmente, porém com exemplos de frases para cada uma das *Intents* sendo testadas, segundo o formato abaixo:

```
## História de teste 1
* definicao_tais: quem é a tais?
    - utter_definicao_tais
    - utter_objetivo
* afirmar: sim
    - utter_processo_como_funciona
* afirmar: sim
   - utter_cadastro_salic_video
   - utter_cadastro_salic_video
* afirmar: quero
    - utter_salic_cadastro_usuario
    - utter_continuar_conversa
* negar: não senhora
    - utter_despedir
```

Uma vez que os arquivos de teste foram adicionados ao diretório correto, basta rodar os testes com a *task* da TAIS:

```sh
sudo docker-compose run --rm bot make test-stories
```

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
Ou rode com docker (atualmente nem sempre funciona o mapeamento de porta - issue #441):

```
docker-compose up
```

Acesse a pagina em `http://localhost:4000`.

# Passos necessários para gerar uma nova release

A criação de uma nova versão Release é bem simples. Os seguintes passos são necessários para lançar uma nova versão

- edite o [CHANGELOG.rst](./CHANGELOG.rst), crie uma nova seção para a release e crie uma nova master loggins section
- Edite o guia de migração para dar assistência para usuários atualizarem para a nova versão
- Commite todas as mudanças acima e gere uma tag para a nova versão usando

```sh
git tag -f 0.7.0 -m "Some helpful line describing the release"
git push origin 0.7.0
```

# Tecnologias do Projeto:
- [Rasa](http://rasa.com) - Inteligência Artificial do Bot
- [RocketChat](https://rocket.chat) - Mensageiro de comunicação do Bot
- [Django](https://www.djangoproject.com) - Site para beta testers
- [Jupyter Notebook](https://jupyter.org) - Notebooks para análise da estrutura de intents e stories
- [Elasticsearch](https://www.elastic.co/pt/) - Para coleta de dados para análise
- [Kibana](https://www.elastic.co/pt/products/kibana) - Análise dos dados coletados a partir das conversas
- [Docker](https://www.docker.com) - Os ambientes são todos dockerizados

# Como Contribuir

Ficaremos muito felizes de receber e incorporar suas contribuições. Tem algumas informações adicionais sobre o estilo do código e a documentação.

Em geral o processo é bem simples:

- Crie uma issue descrevendo uma feature  que você queira trabalhar (ou olhe as issues com o label `help-wanted` e `good-first-issue`)
- Escreva seu código, testes e documentação
- Abra um pull request descrevendo as suas alterações propostas
- Seu pull request será revisado por um dos mantenedores, que pode levantar questões para você sobre eventuais mudanças necessárias ou questões.

Leia o [Guia de Contribuição](./docs/CONTRIBUTING.md) para melhores informações.

# Como conseguir ajuda

Parte da documentação técnica do framework da Tais está disponível na [wiki do repositório](https://github.com/lappis-unb/tais/wiki). Caso não encontre sua resposta, abra uma issue com a tag `duvida` que tentaremos responder o mais rápido possível.

Em caso de dúvidas em relação ao Rasa, veja o grupo [Telegram Rasa Stack Brasil](https://t.me/RasaBrasil), estamos lá também para ajudar.

Veja mais informações de contato em nosso site: https://lappis.rocks

# Licença

Todo o framework da Tais é desenvolvido sob a licença [GPL3](https://github.com/lappis-unb/tais/blob/master/LICENSE)

Veja a lista de dependências de licenças [aqui](https://libraries.io/github/lappis-unb/tais)

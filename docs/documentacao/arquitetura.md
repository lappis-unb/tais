---
layout: page
permalink: /documentacao/arquitetura/
title: Arquitetura
---
A arquitetura geral do framework desenvolvido pelo Laboratório é mostrado na figura abaixo. Foi desenvolvido com a Licença AGPL3.

![](./assets/arquitetura_tecnica.png)

# Ferramentas que compõem o framework

## Rasa NLU
O Rasa NLU é uma ferramenta de processamento de linguagem natural utilizado para a classificação de intenções e extração de entidades aplicadas ao Bot, ou seja, o NLU é responsável por entender o que os usuários escreveram. Isso é feito por uma comparação da mensagem do usuário com os modelos de Machine Learning, procurando inferir a intenção mais próxima da base de conhecimento. A partir daí, a saída do Rasa NLU será a intenção do usuário que enviou a mensagem, que pode ser, por exemplo, cumprimentar, despedir ou uma dúvida específica.

## Rasa Core
O Rasa Core é o centro do chatbot, o que é um diferencial do Framework LAPPIS. Ele é responsável por escolher a melhor ação a ser tomada a partir do histórico da conversa e da atual intenção do usuário. Seja essa ela uma resposta dentro do contexto atual da conversa ou uma ação realizada em um novo contexto. Isso garante que o usuário esteja sempre no controle da conversa, ao invés de ser conduzido por uma árvore de decisões. Assim como o Rasa NLU, o Rasa Core utiliza Machine Learning para responder as mensagens. Para que isso seja possível, é necessário a criação das stories, que são os exemplos de intenção e resposta, ou seja, o chatbot vai escolher a melhor resposta para interagir com os usuários a partir desses exemplos de conversas implementados.

## Jupyter Notebooks
Uma das maiores dificuldades ao projetar o conteúdo e diálogos de um chatbot é a construção adequada do conjunto de dados de treinamento para as intents e as stories. Jupyter Notebooks é uma aplicação web que ajuda a entender e visualizar dados e resultados de análises, facilitando a experimentação, colaboração e publicação online. O Jupyter foi a ferramenta escolhida para automatizar a análise do conteúdo do chatbot e gerar recomendações de ajustes nas intents e stories. O que nos permite antecipar os problemas de interação com o chatbot antes de colocar o conteúdo em produção.

## Elasticsearch/Kibana
É impossível fazer gestão de atendimento sem entender como os cidadãos usam e se apropriam dos canais oferecidos. Conhecer as estatísticas de uso, perfis dos usuários e tendências das demandas é crucial para o sucesso permanente da estratégia. O Elasticsearch é a fundação do módulo de análise de uso do chatbot, pois nele são gerenciadas as informações coletadas das conversas. Para interpretação de todo o conteúdo coletado pelo Elasticsearch, o Kibana é a camada visual responsável por disponibilizar todos os dados por meio de dashboards, gráficos e imagens. Apresenta esses dados de forma a facilitar a interpretação.

## RocketChat
O RocketChat é um software criado por uma startup brasileira que tem o objetivo de fornecer uma infraestrutura de salas de conversa que podem ser utilizadas para diversos fins. Tem recursos de conversação, repositório de documentos e API para bots. Sua interface se assemelha com a do WhatsApp ou Telegram. Seu código é livre e licenciado em MIT. No framework do assistente virtual, o RocketChat carrega a janela de conversação onde os cidadãos interagem de fato com o assistente.

# Perfis que compõem o framework

## Líder de produto
O líder de produto é um perfil fundamental, responsável por orientar o time em relação à aplicação prática do assistente no caso concreto. É o líder de produto que vai estar mais próximo ao órgão para compreender como o assistente virtual se encaixa na estratégia de atendimento da organização. A partir disso, define o escopo da base de conhecimento do bot e prioriza as principais demandas de evolução de conteúdo e novas funcionalidades.

## Engenheiro de software
O time de Engenharia de Software tem como principal objetivo manter e evoluir o framework. Garantir a integração entre as partes e a estabilidade da solução tecnológica. Sempre que uma das partes evolui nas suas comunidades de origem (ex: Rasa, RocketChat, etc) é papel desse time avaliar os impactos da atualização dos componentes no framework Lappis. Também é o time que garante a entrega contínua, ou seja, o processo automatizado de atualizações dos ambientes de homologação e produção.

## Cientista de dados
O cientista de dados tem o papel de analisar os dados relativos ao conteúdo de interação do assistente virtual e as estatísticas de monitoramento. Seu papel é importante para identificar gargalos de pontos de melhoria nos outros módulos. Esse tipo de análise é capaz de identificar quando uma determinada intenção do usuário não está sendo adequadamente interpretada pelo aprendizado de máquina e levantar esse alerta para o time de conteúdo, que pode produzir textos mais claros e para o time de engenharia que pode trabalhar em uma melhor calibragem do aprendizado de máquina. Complementarmente, a análise dos dados de acesso e interação pode produzir novas demandas de cruzamento e visualização de dados para serem implementadas nas ferramentas de visualização dos dados, como o Kibana. Esse tipo de análise é de especial importância para que a ferramenta produza dados que serão agregados nos indicadores de melhoria de atendimento do órgão.

## Roteirista de chatbot
O roteirista de bot tem a responsabilidade de adaptar os conteúdos das políticas fornecidos pelo orgão para que se adequem ao formato conversacional do bot. Para isso ele é responsável por definir a persona do bot a partir de características básicas de personalidade (como empatia, objetividade, nível do vocabulário etc). Uma vez definidas e pactuadas com o órgão, essas características servem de base para a formulação dos textos das respostas disponíveis no banco de conhecimento da assistente virtual. Também é papel do roteirista interpretar os dados de interação e fazer melhorias nos conteúdos que eventualmente não estiverem sendo compreendidos pelos usuários.

## Especialista em UX
A pessoa responsável pela experiência de usuário (UX) trabalha lado-a-lado com a equipe de roteiristas. Especialistas de UX atuam para otimizar a experiência de conversa e reforçar a ideia de uma interação que flui naturalmente. Garantem que sequências de pergunta-resposta se desenvolvam de forma harmônica tanto dentro do mesmo tópico, quanto de forma global na base de conhecimento.

<!-- Explicação da Arquitetura e o funcionamento geral de cada componente -->

# Descrição da Arquitetura

A arquitetura da TAIS é dividida pode ser dividida em 4 submódulos principais:

- (A) Trainer
- (B) Bot
- (C) Business Analytics
- (D) Distribution

## Trainer

Por padrão, em *bots* desenvolvidos com Rasa, os arquivos de treinamento e modelos estão juntos aos arquivos de configuração referentes à forma como o *bot* será executado, como scripts de configuração e utilização do *bot*.

Dentro da TAIS, foi feito um esforço para desacoplar a parte de gerenciamento de conteúdo e treinamentos, da parte de utilização do *bot*.

Analisando a lógica de funcionamento de chatbots `Rasa`, percebeu-se que os esforços aplicados no desenvolvimento de um *bot* estão aplicado em duas categorias:

 - Esforços aplicados na definição da base de conhecimentos do bot e na configuração da estratégia de treinamento. As atividades desenvolvidas estão focadas na configuração correta dos parâmetros da rede, em um bom desenvolvimento dos diálogos, fluxos de interação e personalidade do *bot*, etc.
Resumidademente, ao fim deste conjunto de esforços, o objetivo é garantir a geração de um bom modelo, que reflita bem as características do contexto, possua uma boa acurácia e seja confiável.

 - Atividades focadas na lógica de execução e utilização do *bot*. Aqui há uma maior preocupação com a lógica de negócio e o desenvolvimento é focado em definir os canais de comunicação que serão utilizados, estratégias de escalabilidade e configuração do *bot*.

Uma vez que a responsabilidade por estes dois conjuntos está desacoplada, é mais fácil criar estratégias para versionamento do conteúdo, escalabilidade e distribuição dos serviços utilizados.

Dentro da arquitetura da TAIS utiliza-se serviços baseado em `Docker`, sendo assim existem dois serviços, cada um sendo responsável por uma das categorias acima.

A imagem `docker` utilizada no serviço de *Trainer* é construída a partir do `Dockerfile` abaixo. É nesta imagem onde estarão os diretórios de `intents` e `stories` do `Rasa` que formam a base de conhecimentos do *bot*. Também é nesta imagem onde estarão os modelos treinados.

```Dockerfile
FROM lappis/botrequirements:latest

COPY ./coach /coach
COPY ./scripts /scripts

RUN mkdir /src_models

WORKDIR /coach

RUN make train

RUN find /. | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```

A imagem `lappis/botrequirements:latest` possui todas as dependências `Rasa` pré instaladas e é utilizada como base para este serviço e o serviço de bot, explicado na próxima seção deste documento.

Uma vez que os parâmetros da rede estão bem definidos e o *dataset* do *bot* está finalizado, o processo de treinamento será realizado apenas uma vez, e o mesmo modelo será utilizado sempre que se desejar executar aquele estado de treinamento. Com essa abordagem o versionamento dos modelos do *bot* é feito a partir das *tags* do `docker`, sendo que cada *tag* da imagem de *trainer* reflete uma versão da base de conhecimentos e das configurações de rede utilizadas em um determinado momento.

Isto permite criar facilmente estratégias como a representada no diagrama acima onde se tem dois *bots* que utilizam a mesma versão de modelo, sendo que um dos *bots* utiliza o `Telegram` como canal de interação e o outro utiliza o `RocketChat` como canal. Para a implementação bastaria que houvessem dois serviços com lógicas de conexão diferentes que utilizam a mesma imagem de *trainer* como base.

## Bot

O Bot se utiliza dos modelos pré-treinados do *trainer* e do `Rasa` para execução do *bot*. Este módulo é utilizado também através de um serviço executado à partir de um *container* `Docker`. A imagem utilizada neste serviço é gerada à partir do Dockerfile abaixo:

```Dockerfile
FROM lappis/coach:latest as coach

FROM lappis/botrequirements:latest

COPY ./bot /bot
COPY --from=coach /src_models/ /models/
COPY ./scripts /scripts

WORKDIR /bot

ENV ROCKETCHAT_URL=rocketchat:3000         \
    MAX_TYPING_TIME=10                     \
    MIN_TYPING_TIME=1                      \
    WORDS_PER_SECOND_TYPING=5              \
    ROCKETCHAT_ADMIN_USERNAME=admin        \
    ROCKETCHAT_ADMIN_PASSWORD=admin        \
    ROCKETCHAT_BOT_USERNAME=tais           \
    ROCKETCHAT_BOT_PASSWORD=tais           \
    ENVIRONMENT_NAME=localhost             \
    BOT_VERSION=last-commit-hash           \
    ENABLE_ANALYTICS=False                 \
    ELASTICSEARCH_URL=elasticsearch:9200   

RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```

Quando se utiliza um `Dockerfile` a linha definida com a palavra `FROM` indica a imagem a ser utilizada como base. A partir da imagem de base, os comandos seguintes serão aplicados sequencialmente para ao fim gerar a imagem final.

No `Dockerfile` acima pode-se notar que a palavra `FROM` foi utilizada duas vezes, o objetivo disto é utilizar um recurso do `docker` chamado [multi-stage build](https://docs.docker.com/develop/develop-images/multistage-build/).

O que a linha `FROM lappis/coach:latest as coach` faz é criar uma referência à imagem `lappis/coach` com o nome de `coach`.
Depois disso a imagem de base é redefinida na linha `FROM lappis/botrequirements:latest` como sendo a imagem de *requirements* onde já estão instaladas as dependências do `Rasa` necessárias para a execução do *bot*.
Como a referência à primeira imagem de base foi definida como `coach`, na linha `COPY --from=coach /src_models/ /models/` o diretório de modelos pode ser copiado da primeira imagem de base para a segunda imagem de base. O resultado disso é que a imagem final será criada a partir da imagem `lappis/botrequirements:latest`, mas dentro dela estarão os modelos copiados da imagem `lappis/coach:latest`.

## Business Analytics

O foco das ferramentas e estratégias utilizadas na camada de *Analytics* é aferir e melhorar a qualidade do bot, levando em conta que a qualidade nesse contexto está relacionada às métricas de **acurácia do bot** e **desempenho durante a interação com o usuário**.

O primeiro conjunto de ferramentas utilizado para tal é uma *stack* [ElasticSearch](https://www.elastic.co/), com o uso da ferramenta `Kibana` para visualização dos dados. Esses serviços também são executados utilizando *containers* `Docker`.

As imagens abaixo exemplificam dashboards de visualização de dados da TAIS.

![](./assets/kibana_dados.png)
![](./assets/kibana_dados_2.png)

Para a *Stack* de *Analytics* com o ElasticSearch é utilizado um [script de tracker](https://github.com/lappis-unb/tais/blob/master/bot/tracker_store.py) que sobreescreve o *tracker* de dados padrão do `Rasa`, e faz com que toda vez que uma mensagem seja trocada entre o *bot* e o usuário seja criado uma instância de um objeto de mensagem e este seja inserido no ElasticSearch.

Outras das ferramentas utilizadas é o [Jupyter](https://jupyter.org/), ele é utilizado para avaliar a acurácia das `intents` e `stories` definidas. [Neste outro documento](./notebooks.md) são explicados os parâmetros de avaliação e a utilização dos *notebooks* na TAIS.

Para utilização dos *notebook* é utilizado um serviço `docker` que, ao rodar, terá uma porta compartilhada entre o *container* e o computador e dará acesso aos códigos que executam as métricas. A execução e análise dessas métricas ainda é feita de forma manual, e deverá ser feita subjetivamente de acordo com o contexto de cada *bot*.

## Distribution

A última camada é a camada de apresentação e distribuição. É a camada onde acontecerá o contato direto do usuário e o meio por onde se dará a experiência de interação com o *bot*.

O Rasa provê nativamente [conectores](https://rasa.com/docs/core/0.9.8/connectors/) para algumas ferramentas como: RocketChat, Slack, Telegram, Mattermost e Twillio.

Na TAIS, é utilizado o RocketChat como canal principal de interação. Uma vez que se configura um agente de conversação dentro do RocketChat, é possível gerar um código `javascript` que permite a renderização de uma janela de conversação com o *bot*.  Essa abordagem permite uma flexibilidade muito grande, uma vez que quando o *bot* está propriamente configurado, este código pode ser injetado em qualquer pagina que será carregada pelo usuário, que não precisará criar uma conta ou acessar diretamente o servidor do `RocketChat` para conversar com o *bot*.

![](./assets/home_tais.png)

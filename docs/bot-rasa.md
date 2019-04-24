---
layout: page
title: Tais com Rasa
permalink: /rasa-bot/
---

# Tais com Rasa
## O que é a Tais?
A Tais, Tecnologia de Aprendizado Interativo Salic, é uma assistente virtual de suporte para o Sistema de Apoio às Leis de Incentivo à Cultura, o Salic.

## O que é o Rasa?
O Rasa é um conjunto de ferramentas _open source_ de _machine learning_ para desenvolvedores com função de criar, melhorar e desenvolver chatbots e assistentes virtuais baseados em reconhecimento de texto e voz.

> Machine Learning: O aprendizado de máquina, em inglês, machine learning, é um método de análise de dados que automatiza a construção de modelos analíticos. É um ramo da inteligência artificial baseado na ideia de que sistemas podem aprender com dados, identificar padrões e tomar decisões com o mínimo de intervenção humana.

> Open Source: Open source é um termo em inglês para código aberto que diz respeito ao código fonte de um software de utilização livre que é disponibilizado, de maneira online pelos desenvolvedores, podendo ter acesso a elas qualquer pessoa, sem restrições.

## Desenvolvimento da Tais
Durante o desenvolvimento da Tais diversas ferramentas foram estudadas e testadas antes da decisão de qual tecnológia seria escolhida de base para o projeto. Dentre essas ferramentas, o Rasa NLU e o Rasa Core se destacaram devido ao desempenho que possuem, por de serem flexíveis em relação as ferramentas compatíveis com o módulo de backend e por utilizarem a licença permissiva **Apache License 2.0**.
Mais informações sobre o estudo de tecnológias podem ser acessados na página [Estudo sobre ferramentas de bots](https://github.com/lappis-unb/tais/wiki/Estudo-sobre-ferramentas-de-bots). 

### Arquitetura do Rasa
O Rasa Core possui uma a seguinte arquitetura de funcionamento:

<img src="https://i.imgur.com/i8T1Z76.png" alt="drawing"/>

Esse diagrama segue os seguintes passos:
* 1: A messagem é recebida e passada para o Interpreter, que a converte em um dicionário incluindo o texto original, a intent, e qualquer entity que for encontrada;
* 2: O Tracker é o objeto que mantém controle do estado da conversa. Ele recebe a informação de que uma nova mensagem foi recebida;
* 3: O Policy recebe as informações atuais do Tracker;
* 4: O Policy decide qual ação deve ser tomada;
* 5: A ação escolhida é captada pelo Tracker;
* 6: A resposta é enviada para o usuário.

Essa arquitetura possibilita a conexão com diversas plataformas de comunicação para estruturação do bot, que varia de acordo com a necessidade do projeto. O modo de efetuar essa conexão pode ser visto na parte de [Chat & Voice platforms](https://rasa.com/docs/core/connectors/) da documentação do Rasa Core.

### Criação/Atualização de conteúdos
Existem três pontos principais que relacionam os conteúdos analisados pelo bot dentro do Rasa, eles são as **Intents**, as **Utters** e as  **Stories**.
As intents fazem referências as possíveis frases enviadas por usuários. Essas, por sua vez, são enviadas para o Rasa NLU que aplica diversos algoritmos de linguagem natural para extrair a intenção da setença.
As Utters são as ações de respostas do bot para as intenções do usuário.
Essa relação Utter-Intent é mapeada nas Stories, fornecendo ao bot uma base de possíveis diálogos e permitindo que ele gere novas relações e fluxos de conversa.

* ### Intents
    De forma mais específica, as intents são exemplos de frases que um usuário poderia falar para o assistente com intenção de se referir a um assunto determinado. Elas podem ser encontradas na pasta `/bot/data/intents` e ficam salvas em um arquivo markdown. 
    Uma intent deve ser escrita da seguinte forma:
    `## intent:<nome_da_intent>`
	`- <exemplo de frase>`
	`- <texto>`
    `- <texto>`
	Após criada, uma intent deve ser inserida no arquivo `/bot/domain.yml`, na área de intents, da seguinte forma:
	`<!-- área de intents -->`
	`intents:`
	`<!-- inserção da intent -->`
	`	- <nome_da_intent>`

* ### Utters
	As utters ficam localizadas no arquivo `/bot/domain.yml` e são os textos de resposta do bot para uma intent. Elas devem ser inseridas na área de templates a partir do seguinte modelo:
	`<!-- área de templates -->`
	`templates:`
	`<!-- inserção da utter -->`
	`	utter_<nome_da_utter>:`
    `		- text: |`
    `			<texto_de_resposta>`
    e também deve ser listada na área de actions:
    `<!-- área de actions -->`
	`actions:`
	`<!-- inserção da utter -->`
	`	- utter_<nome_da_utter>`

* ### Stories
	A criação das stories envolvem as Intents e Utters já existentes no bot. Elas podem ser encontradas na pasta `/bot/data/stories` e ficam salvas em um arquivo markdown, assim como as intents. Elas podem envolver diversas intents e utters e devem ser feitas no seguinte padrão:
	`## <nome_da_storie>`
	`* <nome_da_intent_1>`
	`	- utter_<nome_da_utter_1>`
	`* <nome_da_intent_2>`
    `	- utter_<nome_da_utter_2>`
	`* <nome_da_intent_3>`
    `	- utter_<nome_da_utter_3>`
    `	- utter_<nome_da_utter_4>`
    As stories não precisam ser listadas no arquivo `/bot/domain.yml`

> Exemplos retirados dos arquivos "captacao.md", "domain.yml" e "dinheiro.md", da Tais.

### Outras funcionalidades
O Rasa Core proporcina diversas funcionalidades para o projeto ao qual é aplicado, como a alteração das configurações de resposta padrão do bot (que pode ser visto no arquivo `/bot/fallback.py`) e CustomActions, por exemplo. Essas funcionalidades podem ser estudadas a partir da documentação oficial do [Rasa](https://rasa.com/docs/core). 

## Referências
* https://canaltech.com.br/produtos/O-que-e-open-source/, acessado 23/04/2019
* https://github.com/RasaHQ, acessado 23/04/2019
* https://www.sas.com/pt_br/insights/analytics/machine-learning.html, acessado 23/04/2019
* https://rasa.com/docs/core/architecture/, acessado 23/04/2019

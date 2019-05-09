---
layout: page
title: Tais com Rasa
permalink: /rasa-bot/
---

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

Já o Rasa _NLU_ atua na parte de interpretação da linguagem natural. De modo mais específico, Rasa NLU é uma biblioteca _NLP_ para classificação de intenções e extração de entidades, isso é, a frase enviada pelo usuário é passada para o Rasa NLU onde são aplicados diversos algoritmos para definir qual a provável intenção da sentença a partir da lista de intenções previamente fornecida pelo desenvolvedor.
Mais detalhes do funcionamento do Rasa NLU podem ser lidos na documentação oficial do [Rasa](https://rasa.com/docs/nlu/).

> NLU: Natural Language Understanding
> NLP: Natural Language Processing 

### Criação/Atualização de conteúdos
Existem três pontos principais que relacionam os conteúdos analisados pelo bot dentro do Rasa, eles são as **Intents**, as **Utters** e as  **Stories**.

* ### Intents
	As intents fazem referências as possíveis intenções que o usuário possui ao enviar mensagens, o processamento dessas mensagens para classificação da intent é feito pelo Rasa NLU, como foi explicado acima. Podem ser encontradas na pasta `/bot/data/intents` e ficam salvas em um arquivo markdown. O arquivo de Intent deve possuir diversas frases de exemplo para que o bot possa ter uma base para a análise no NLU.
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
	As Utters são as mensagens de respostas enviadas pelo bot para o usuário após a detecção de uma intent. Ficam localizadas no arquivo `/bot/domain.yml`. Elas devem ser inseridas na área de templates a partir do seguinte modelo:
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
	A relação Utter-Intent é mapeada nas Stories, fornecendo ao bot uma base de possíveis diálogos e permitindo que ele gere novas relações e fluxos de conversa. Sua criação envolve as Intents e Utters já existentes no bot. Elas podem ser encontradas na pasta `/bot/data/stories` e ficam salvas em um arquivo markdown, assim como as intents. Elas podem envolver diversas intents e utters e devem ser feitas no seguinte padrão:
	`## <nome_da_storie>`
	`* <nome_da_intent_1>`
	`	- utter_<nome_da_utter_1>`
	`* <nome_da_intent_2>`
    `	- utter_<nome_da_utter_2>`
	`* <nome_da_intent_3>`
    `	- utter_<nome_da_utter_3>`
    `	- utter_<nome_da_utter_4>`
    As stories não precisam ser listadas no arquivo `/bot/domain.yml`

Para uma melhor compreensão de como se criar intents é recomendada a leitura do texto [Intents Eficientes](https://github.com/lappis-unb/tais/wiki/Intents-Eficientes).

### Outras funcionalidades
O Rasa Core proporcina diversas funcionalidades para o projeto ao qual é aplicado, como a alteração das configurações de resposta padrão do bot (que pode ser visto no arquivo `/bot/fallback.py`) e CustomActions, por exemplo. Essas funcionalidades podem ser estudadas a partir da documentação oficial do [Rasa](https://rasa.com/docs/core). 

## Referências
* https://canaltech.com.br/produtos/O-que-e-open-source/, acessado 23/04/2019
* https://github.com/RasaHQ, acessado 23/04/2019
* https://www.sas.com/pt_br/insights/analytics/machine-learning.html, acessado 23/04/2019
* https://rasa.com/docs/core/architecture/, acessado 23/04/2019
* https://rasa.com/products/rasa-nlu/, acessado 24/04/2019
* https://rasa.com/docs/core/domains/#utter-templates, acessado 24/04/2019
* https://rasa.com/products/rasa-nlu/, acessado 24/04/2019

<!-- 
## O que é o RASA

## Lexicos
* **Intent:** Possíveis frases que um usuário enviariam para falar sobre um determinado tópico. Servem de base para o treinamento de análise de linguagem natural do chatbot, que as manipula para reconhecer frases não listadas.
* **Utter:** Ação de resposta do bot após uma intent ser acionada. É a resposta do bot para o usuário após receber uma mensagem.
* **Storie:** Local onde se determina qual Utter se relaciona com qual Intent. Também serve para explicitar possíveis fluxos de conversa que o bot terá.

## Como funciona intents, Utters e Stories

Intents e Stories podem ser encontradas na pasta bot/data, ondem ficam listadas em suas respectivas pastas, já as Utters ficam listadas no arquivo domain.yml, encontrado na pasta bot.
Para gerar mais conteúdo para o chatbot é necessário criar uma nova Intent, gerar exemplos de frases do usuário, em seguida criar a Utter de resposta para essa Intent e por fim criar uma Storie que relacione as duas. Todas Utter, Intents e Stories devem ser listada no arquivo domain.yml. -->

<!-- Explicar o funcionamento da Tais com Rasa -->


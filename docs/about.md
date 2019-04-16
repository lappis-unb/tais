---
layout: page
title: Quem é a Tais?
permalink: /about/
---

## Tais no contexto do MinC
<!-- Explicação geral do objetivo da Tais no MinC -->

A Tais, Tecnologia de Aprendizado Interativo Salic, é uma assistente virtual de suporte para o Sistema de Apoio às Leis de Incentivo à Cultura, o Salic. Desenvolvida pelo Laboratório Avançado de Produção, Pesquisa e Inovação em Software (Lappis) da Universidade de Brasília (FGA/UnB), em parceria com o Ministério da Cultura, tem como função tirar dúvidas do público sobre a Lei Rouanet e o Salic e responde a questões básicas de forma simplificada, com objetivo de apoiar os cidadãos no entendimento.

* Salic <!-- Explicação do que é o Salic-->
O Salic, Sistema de Apoio às Leis de Incentivo à Cultura, é um sistema unificado, utilizado para apresentação de propostas e acompanhamento de projetos culturais. Todas as fases de tramitação, da admissibilidade à prestação de contas, estão registradas e automatizadas no sistema. O Salic proporciona acesso a dados da Lei Rouanet como o número de propostas apresentadas, os projetos aprovados e os recursos captados – por período de tempo, linguagem cultural ou região / estado do País.

* MinC <!-- Explicação do que é o Minc -->
Ministério da Cultura (MinC) foi um ministério do governo brasileiro responsável pelas letras, artes, folclore e outras formas de expressão da cultura nacional e pelo patrimônio histórico, arqueológico, artístico e cultural do Brasil e tinha como objetivo promover o crescimento cultural, ampliar o acesso à cultura e fortalecer a economia criativa em todas as regiões do país, contribuindo para o desenvolvimento do Brasil.

#### Léxicos:
<!-- Explicação de termos utilizados -->
* Intent: Possíveis frases que um usuário enviariam para falar sobre um determinado tópico. Servem de base para o treinamento de análise de linguagem natural do chatbot, que as manipula para reconhecer frases não listadas.
* Utter: Ação de resposta do bot após uma intent ser acionada. É a resposta do bot para o usuário após receber uma mensagem.
* Storie: Local onde se determina qual Utter se relaciona com qual Intent. Também serve para explicitar possíveis fluxos de conversa que o bot terá.
							
Intents e Stories podem ser encontradas na pasta bot/data, ondem ficam listadas em suas respectivas pastas, já as Utters ficam listadas no arquivo domain.yml, encontrado na pasta bot.
Para gerar mais conteúdo para o chatbot é necessário criar uma nova Intent, gerar exemplos de frases do usuário, em seguida criar a Utter de resposta para essa Intent e por fim criar uma Storie que relacione as duas. Todas Utter, Intents e Stories devem ser listada no arquivo domain.yml.

## Tais no Lappis
<!-- Explicação geral da história da Tais no Lappis -->
A Tais foi o primeiro chatbot desenvolvido pelo Lappis, gerando diversas pesquisas e estudos sobre a área e, desse modo, ampliando os conteúdos desenvolvidos pelo laboratório. 

A construção de um chatbot é um grande desafio e exige perfis em diferentes áreas como desenvolvedores, roteiristas de bot e designers com foco em Ux e essas exigencias resultaram em pesquisas como:
* [Ferramentas de bots](https://github.com/lappis-unb/tais/wiki/Estudo-sobre-ferramentas-de-bots)
* [Melhores práticas de bots](https://github.com/lappis-unb/tais/wiki/Estudo-sobre-melhores-pr%C3%A1ticas-de-bots)
* [Pipeline do RASA](https://github.com/lappis-unb/tais/wiki/Estudo-sobre-pipeline-ML-Rasa)
* [Intents eficientes](https://github.com/lappis-unb/tais/wiki/Intents-Eficientes)
* [Refinamento da Taís](https://github.com/lappis-unb/tais/wiki/Tais-Refinamento-v2.0)
* [Ferramentas de edição de conteúdo](https://github.com/lappis-unb/tais/wiki/estudo-de-ferramentas-de-gerenciamento-de-conteudo)
* [Slots e Entidades](https://github.com/lappis-unb/tais/wiki/Uso-de-slots-e-entidades)
* [Teste automatizado](https://github.com/lappis-unb/tais/wiki/Testes-Automatizados)
* [Custom Actions ](https://github.com/lappis-unb/tais/wiki/Estudo-sobre-custom-actions)

E a partir disso novos projetos surgiram, como o [Lappisudo, o bot do Lappis](https://github.com/lappis-unb/lappisudo) e o [Rasa Boilerplate ptbr](https://github.com/lappis-unb/rasa-ptbr-boilerplate).

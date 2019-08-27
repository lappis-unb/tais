---
layout: page
permalink: /tutoriais/tutorial-monitoramento-tais/
title: Tutorial de Monitoramento da Tais
---

# Tutorial de Monitoramento da Tais

O monitoramento da Tais é feito de forma orientada a dados, ou seja, analisamos os dados do Kibana, identificamos as intents que caíram no default (as intents que a Tais não conseguiu responder), e as intents com confiança abaixo de 0,7, para poder melhorá-as. Além disso, lemos as conversas entre a Tais e os usuários para identificar as melhorias que podemos fazer. O que seriam essas melhorias? Tudo que esteja interferindo no entendimento da Tais para que ela consiga ter uma comunicação eficiente com o usuário. A melhor forma de evoluir um chatbot é tendo o contato real de como ele está interagindo com as pessoas, lendo as conversas podemos enriquecer o nosso bot, tornando-o apto para lidar com as situações reais e não somente com as hipóteses que se passaram na nossa cabeça, tal processo garante que ele se torne cada dia mais eficiente. 

## Passo a passo do monitoramento

1 - Primeiro é necessário acessar o Kibana (https://kibana.tais.lappis.rocks/);
2 - No Kibana analisamos a confiança das intents e as intents que caíram no default e as intents com confiança abaixo de 0,7, assim podemos ver quais intents ela não está respondendo com eficiência;
![photo_2019-08-22_18-23-07](https://user-images.githubusercontent.com/42178586/63554020-9e740e80-c512-11e9-9a63-78a6c5f5fc39.jpg)

3 - Após a análise do Kibana é necessário acessar as conversas dos usuários (https://lappis.cultura.gov.br/);
![photo_2019-08-22_19-39-19](https://user-images.githubusercontent.com/42178586/63554783-062b5900-c515-11e9-9731-29cef85d6b00.jpg)

4 - Leia as conversas e anote os bugs separando-os em categorias de bugs, é imprescindível a leitura das conversas, pois só assim tomamos conhecimento sobre o contexto e conseguimos criar a melhor estratégia para consertá-lo: 
atualização de intents (melhorar intent),
atualização de stories (melhorar stories),
atualização de conteúdo (melhorar utter+intent),
inserir conteúdo novo (utter+intent+story),
melhoria de utter (melhorar a escrita da utter, deixá-las mais compreensível);
5 - Faça uma análise de quais bugs podem ser consertados imediatamente e quais precisam de mais maturidade da Tais;
6 - Conserte os bugs imediatos, todos que estão ao nosso alcance e que não vão afetar a Tais;
![photo_2019-08-22_19-39-15](https://user-images.githubusercontent.com/42178586/63554768-f6137980-c514-11e9-91c3-d44fb092cd49.jpg)

7 - Anote os bugs que precisam de maturidade para quando surgir a oportunidade, quais seriam esses bugs? Um exemplo disso seria um assunto que é muito complexo e ela ainda não conseguiria responder no momento por limitações tecnológicas, assuntos que no momento confundiria a Tais. Como tentar fazer a Tais entender quando o usuário conta a história do seu objetivo, no momento, ela não consegue fazer isso mesmo que a gente tente atualizar e criar intents para isso, pois cada usuário possui uma história muito peculiar e difícil de ser mapeada.

## Como solucionar bugs

Em cada conversa analisada é preciso anotar os bugs encontrados, quando a Tais possui o conteúdo perguntado mas não identificou a pergunta do usuário é um problema de atualização de intents, neste caso temos que procurar a intent existente e melhorá-la sem que isso afete a precisão das outras intents que existem.
Quando a Tais tem o conteúdo perguntado e também possui em sua intent o exemplo de pergunta que o usuário usou, neste caso provavelmente será um problema de contexto, ela não conseguiu entender a pergunta naquele momento, para solucionar este tipo de bug devemos fazer uma atualização de stories relacionadas ao contexto daquela pergunta, ou seja, devemos construir um caminho no fluxo que permita que ela entenda aquela pergunta naquele dado momento.
Alguns conteúdos que a Tais já possui podem ser otimizados, por exemplo se ela responde sobre determinado prazo, e temos uma pergunta se tal prazo pode ser prorrogado, podemos juntar os dois assuntos e fazer uma atualização de conteúdo. Neste caso, devemos melhorar tanto a utter quanto a intent relacionadas a este conteúdo.
Há também os novos assuntos que a Tais não sabe responder. Deste modo, temos também o procedimento de inserir conteúdo novo, nesta etapa temos que analisar quais conteúdos podem ser inseridos sem diminuir a eficiência da Tais, e quais ela ainda não tem maturidade para responder neste momento, o importante é sempre deixar anotado tudo isso para que um dia tal conteúdo possa fazer parte do seu repertório de informações.Quando um usuário pergunta, a Tais responde corretamente, mas mesmo assim ele não se sente contemplado com a resposta precisamos fazer uma melhoria de utter, temos que melhorar o texto da Utter para que ela fique mais clara e consiga sanar as dúvidas do usuário.
A Tais está constantemente aprendendo a se comunicar melhor, a ser mais gentil e mais polida, sendo assim temos a parte de melhoria de interação, nela criamos modos de fazer ela ser cada vez mais humana, como por exemplo responder a um obrigada, a um tudo bem, entre outras façanhas que fazem parte da nossa comunicação quotidiana. Estes são apenas algumas classes de bugs que foram encontradas, com toda certeza na medida em que a Tais for evoluindo vamos encontrar novas formas de atualizá-la e consequentemente surgirão novos problemas e novas classes de Bugs.

## Frequência e performance

Recomenda-se que o monitoramento seja feito diariamente, é preciso que haja uma pessoa dedicada a esta função para sanar os bugs e implementar as melhorias necessárias.  Em três sprints (um mês e meio) de monitoramento foram feitas 19 issues, sendo:

1 issue de retirada de conteúdo;

10 issues de inserir conteúdo novo;

2 issues de melhoria de utter

5 issues de atualização de Intents

1 issue de atualização de Stories

# Referência

[Aperfeiçoamento da Tais](https://lappis-unb.github.io/tais/documentacao/aperfei%C3%A7oamento-da-tais/)
